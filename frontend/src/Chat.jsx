import React, { useEffect, useRef } from 'react';
import io from 'socket.io-client';

const socket = io('http://<JETSON_IP>:8000'); // Replace with your Jetson IP

export default function Chat({ messages, setMessages }) {
  const chatEndRef = useRef(null);

  // Auto-scroll to bottom
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // WebSocket listener
  useEffect(() => {
    socket.on('llama_response', (data) => {
      setMessages(prev => [...prev, { text: data.text, sender: 'llama' }]);
    });

    return () => socket.off('llama_response');
  }, []);

  return (
    <div className="chat">
      {messages.map((msg, i) => (
        <div key={i} className={`message ${msg.sender}`}>
          {msg.text}
        </div>
      ))}
      <div ref={chatEndRef} />
    </div>
  );
}
