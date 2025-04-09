#!/bin/bash
# Install backend dependencies
sudo apt update
sudo apt install -y python3-pip ffmpeg
pip install fastapi uvicorn httpx torch transformers

# Install Whisper.cpp (STT)
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp && make -j4
./models/download-ggml-model.sh small.en

# Install Piper (TTS)
wget https://github.com/rhasspy/piper/releases/latest/download/piper_amd64.tar.gz
tar xvf piper_amd64.tar.gz
./piper --download-voice en_US-lessac-medium
