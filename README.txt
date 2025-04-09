# **Voice-Enabled Llama 2 on NVIDIA Jetson Orin Nano**  
**A real-time, voice-controlled AI assistant optimized for edge deployment**  

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![Jetson Orin](https://img.shields.io/badge/Platform-NVIDIA%20Jetson%20Orin-green)](https://developer.nvidia.com/embedded/jetson-orin)  

---

## **🚀 Overview**  
This project deploys **Meta’s Llama 2** on a **Jetson Orin Nano** with full voice integration:  
- **🎙️ Speech-to-Text (STT):** Convert user voice input to text using optimized Whisper.cpp.  
- **🦙 Llama 2 Inference:** Run quantized (4-bit) Llama 2 locally with TensorRT-LLM.  
- **🔊 Text-to-Speech (TTS):** Generate natural-sounding responses with Piper TTS.  
- **🌐 Web UI:** Interactive chat interface with voice/text input.  

Optimized for **Jetson’s 8GB RAM** using quantization, memory management, and hardware acceleration.  

---

## **🛠️ Technical Framework**  
### **Hardware**  
- **NVIDIA Jetson Orin Nano** (8GB RAM)  
- **Required Peripherals:** Microphone, speakers, and cooling fan (for sustained loads).  

### **Software Stack**  
| Component          | Technology               | Purpose                                  |  
|--------------------|--------------------------|------------------------------------------|  
| **Inference**      | TensorRT-LLM + GPTQ      | 4-bit quantized Llama 2                 |  
| **STT**           | Whisper.cpp              | Low-latency speech recognition          |  
| **TTS**           | Piper                    | Offline, lightweight voice synthesis     |  
| **Backend**       | FastAPI + WebSockets     | Bridge between frontend and AI models    |  
| **Frontend**      | React + Web Audio API    | Voice/chat interface                    |  

---

## **⚙️ Setup Instructions**  

### **1. Clone the Repository**  
```bash  
git clone https://github.com/sicklecells/voice-llama-jetson.git  
cd voice-llama-jetson  
```

### **2. Install Dependencies (Jetson Orin)**  
Run the setup script:  
```bash  
chmod +x scripts/install_deps.sh  
./scripts/install_deps.sh  # Installs Python deps, Whisper.cpp, Piper  
```

### **3. Configure Services**  
- **Llama 2 Model**: Download a 4-bit quantized model (e.g., `TheBloke/Llama-2-7B-Chat-GPTQ`) and place it in `backend/models/`.  
- **Environment Variables**: Set your Jetson’s IP in `frontend/src/App.jsx`.  

### **4. Launch the System**  
```bash  
./scripts/start.sh  # Starts backend, STT, and TTS services  
```

### **5. Access the Web UI**  
From a separate machine (or Jetson’s browser):  
```bash  
cd frontend  
npm install && npm start  # Open http://localhost:3000  
```

---

## **🎯 Key Features**  
- **Optimized for Edge**: 4-bit quantization and CUDA kernels for Jetson Orin.  
- **Real-Time Voice**: <500ms latency for STT → Llama 2 → TTS pipeline.  
- **Memory Management**: Automatic GPU cache clearing between inferences.  
- **Modular Design**: Easily swap STT/TTS models (e.g., Riva for Whisper.cpp).  

---

## **📂 Repository Structure**  
```  
voice-llama-jetson/  
├── backend/                  # FastAPI server and inference  
│   ├── app.py               # REST/WebSocket endpoints  
│   ├── inference.py         # Quantized Llama 2 pipeline  
├── frontend/                # React web interface  
│   ├── src/  
│   │   ├── App.jsx          # Main UI  
│   │   ├── AudioRecorder.js # Voice input handler  
├── scripts/  
│   ├── install_deps.sh      # Jetson setup script  
│   └── start.sh            # Service launcher  
```

---

## **🧠 Memory Optimization Strategies**  
1. **4-Bit Quantization**: Reduces Llama 2’s memory footprint from 14GB → 6GB.  
2. **Streaming Responses**: Token-by-token generation via WebSockets.  
3. **GPU Cache Clearing**: Automatic after each inference (`torch.cuda.empty_cache()`).  
4. **Efficient STT/TTS**: Whisper.cpp and Piper use <1GB RAM combined.  

---

## **🤖 Demo Workflow**  
```mermaid  
sequenceDiagram  
    User->>Frontend: Press 🎤 or type text  
    Frontend->>Backend: Send audio/text  
    Backend->>Whisper.cpp: Transcribe audio  
    Whisper.cpp->>Backend: Return text  
    Backend->>Llama 2: Generate response  
    Llama 2->>Backend: Stream tokens  
    Backend->>Piper TTS: Convert text to speech  
    Piper TTS->>Frontend: Return audio  
    Frontend->>User: Play response  
```

---

## **📜 License**  
MIT License - Free for personal and commercial use.  

---

## **📮 Support**  
For issues or enhancements, open a [GitHub Issue](https://github.com/sicklecells/voice-llama-jetson/issues).  
