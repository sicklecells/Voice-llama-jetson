# Voice-llama-jetson
Voice integrated LLAMA on Jetson Orin Nano

voice-llama-jetson/  
├── backend/                  # FastAPI server (runs on Jetson)  
│   ├── app.py                # STT/TTS/Llama2 endpoints  
│   ├── inference.py          # Optimized Llama 2 inference  
│   ├── requirements.txt      # Python dependencies  
├── frontend/                 # React frontend  
│   ├── public/  
│   │   └── index.html        # HTML entry point  
│   ├── src/  
│   │   ├── App.jsx           # Main UI with voice/text input  
│   │   ├── Chat.jsx          # Real-time chat component  
│   │   └── AudioRecorder.jsx # Voice recording logic  
│   ├── package.json  
├── scripts/  
│   ├── install_deps.sh       # Jetson setup script  
│   └── start.sh             # Launch backend/frontend  
├── README.md
