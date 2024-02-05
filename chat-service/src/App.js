import React, { useState, useEffect, useRef } from 'react';
import io from 'socket.io-client';
import { marked } from 'marked';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [chat, setChat] = useState([]);
  const [username, setUsername] = useState('');
  const [isConnected, setIsConnected] = useState(false);
  const [directCommunication, setDirectCommunication] = useState(false);
  const socketRef = useRef(null);
  const messagesContainerRef = useRef(null);
  const [text, setText] = useState('');

  useEffect(() => {
    if (socketRef.current) {
      socketRef.current.on('message', (msg) => {
        setChat((prevChat) => [...prevChat, msg]);
        setTimeout(() => {
          messagesContainerRef.current.scrollTop = messagesContainerRef.current.scrollHeight;
        }, 0);
      });
      return () => socketRef.current.off('message');
    }
  }, [isConnected]);

  const getMarkdownText = (text) => {
    var rawMarkup = marked(text);
    return { __html: rawMarkup };
  };

  const handleConnect = () => {
    if (username.trim()) {
      socketRef.current = io('http://localhost:5000', {
        query: { username }
      });
      setIsConnected(true);
    } else {
      alert('Please enter your name before connecting.');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    } else if (e.key === 'Enter' && e.shiftKey) {
      setMessage((prevMessage) => prevMessage + '\n');
    }
  };

  const handleCheckboxChange = (event) => {
    if (event.target.checked) {
      socketRef.current.emit("message", "enableDirectCommunication");
    } else {
      socketRef.current.emit("message", "disableDirectCommunication");
    }
    setDirectCommunication(event.target.checked);
  };

  const sendMessage = () => {
    if (username === '') {
      alert('Please enter your name before sending a message.');
      return;
    }
    const messageToSend = `${username}: ${message}`;
    socketRef.current.emit('message', messageToSend);
    setMessage('');
  };

  if (!isConnected) {
    return (
      <div className="connect-container">
        <input
          type="text"
          name="username"
          placeholder="Enter your name"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <button onClick={handleConnect}>Connect</button>
      </div>
    );
  }

  return (
    <div className="chat-container">
      <div className="input-area">
        <div className="top-row">
          <input
            type="text"
            name="username"
            placeholder="Enter your name"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <label>
            <input
              type="checkbox"
              name="directCommunication"
              checked={directCommunication}
              onChange={handleCheckboxChange}
            />
            Enable direct communication
          </label>
        </div>
        <div className="bottom-row">
          <textarea
            rows="4"
            name="message"
            placeholder="Enter your message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyDown}
          />
          <button className="send-button" onClick={sendMessage}>Send</button>
        </div>
      </div>
      <div className="messages-area" id="message-area" ref={messagesContainerRef}>
        {chat.map((msg, index) => (
          <p key={index} dangerouslySetInnerHTML={getMarkdownText(msg)}></p>
        ))}
      </div>
    </div>
  );


}

export default App;
