#!/bin/bash
# Start backend
uvicorn backend.app:app --host 0.0.0.0 --port 8000 &

# Start Whisper.cpp STT server
cd whisper.cpp && ./server -m models/ggml-small.en.bin &

# Start Piper TTS server
./piper --model en_US-lessac-medium.onnx --port 5000 &

# Start frontend (from another machine)
echo "Frontend: cd frontend && npm start"
