import React, { useState, useRef } from 'react';
import axios from 'axios';
import AudioRecorder from './AudioRecorder';
import Chat from './Chat';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [messages, setMessages] = useState([]);
  const [isRecording, setIsRecording] = useState(false);

  const handleTextSubmit = async () => {
    if (!inputText.trim()) return;
    setMessages([...messages, { text: inputText, sender: 'user' }]);
    const response = await axios.post('http://<JETSON_IP>:8000/llama', { text: inputText });
    setMessages([...messages, { text: response.data, sender: 'llama' }]);
    setInputText('');
  };

  return (
    <div className="app">
      <h1>Voice-Enabled Llama 2</h1>
      <Chat messages={messages} />
      <div className="input-area">
        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target)}
          placeholder="Type or use voice..."
        />
        <button onClick={handleTextSubmit}>Send</button>
        <AudioRecorder
          onRecordingComplete={async (audioBlob) => {
            const formData = new FormData();
            formData.append('audio', audioBlob);
            const { data } = await axios.post('http://<JETSON_IP>:8000/stt', formData);
            setInputText(data.text);
          }}
          isRecording={isRecording}
          setIsRecording={setIsRecording}
        />
      </div>
    </div>
  );
}

export default App;
