import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState('');
  const [responseLength, setResponseLength] = useState('medium');
  const [answer, setAnswer] = useState('');

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const uploadPDF = async () => {
    const formData = new FormData();
    formData.append('pdf', file);
    await axios.post('http://localhost:5000/upload', formData);
    alert('PDF uploaded!');
  };

  const askQuestion = async () => {
    const res = await axios.post('http://localhost:5000/ask', {
      question,
      length: responseLength,
    });
    setAnswer(res.data.answer);
  };

  return (
    <div className='app-container'>
      <h1>Chat with PDF</h1>
      <div className='file-upload-section'>
        <input type="file" accept="application/pdf" onChange={handleFileChange} />
        <button onClick={uploadPDF}>Upload PDF</button>
      </div>
      <div className='question-section'>
        <input
          type="text"
          value={question}
          placeholder="Ask a question about the PDF"
          onChange={(e) => setQuestion(e.target.value)}
        />
        <select onChange={(e) => setResponseLength(e.target.value)}>
          <option value="short">Short</option>
          <option value="medium" selected>Medium</option>
          <option value="long">Long</option>
        </select>
        <button onClick={askQuestion}>Ask Question</button>
      </div>

      {answer && (
        <div className='answer-box'>
          <h2>Answer:</h2>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;
