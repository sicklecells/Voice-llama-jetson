from fastapi import FastAPI, WebSocket, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
import torch
import logging

app = FastAPI()

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

# Memory management
def clear_gpu_cache():
    torch.cuda.empty_cache()

# STT endpoint (using Whisper.cpp HTTP server)
@app.post("/stt")
async def stt(audio: UploadFile):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8080/inference",  # Whisper.cpp server
                files={"file": (audio.filename, await audio.read())},
                timeout=30.0,
            )
        return {"text": response.json()["transcription"]}
    except Exception as e:
        logging.error(f"STT error: {e}")
        raise HTTPException(status_code=500, detail="STT failed")

# Llama 2 inference (simplified)
@app.websocket("/ws")
async def llama_chat(websocket: WebSocket):
    await websocket.accept()
    clear_gpu_cache()  # Free memory before inference
    try:
        while True:
            text = await websocket.receive_text()
            # Replace with your Llama 2 inference (TensorRT-LLM/llama.cpp)
            response = f"Llama 2 response to: {text}"
            await websocket.send_text(response)
    finally:
        clear_gpu_cache()

# TTS endpoint (using Piper)
@app.post("/tts")
async def tts(text: str):
    try:
        # Call local Piper TTS server
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:5000/synthesize",
                json={"text": text},
                timeout=30.0,
            )
        return response.content  # Audio binary (WAV)
    except Exception as e:
        logging.error(f"TTS error: {e}")
        raise HTTPException(status_code=500, detail="TTS failed")
