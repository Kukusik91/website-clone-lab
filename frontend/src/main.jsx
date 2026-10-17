import React from 'react';
import { createRoot } from 'react-dom/client';
import './style.css';

function App() {
  const [status, setStatus] = React.useState('Проверяем API…');
  React.useEffect(() => {
    fetch('http://127.0.0.1:8000/api/health')
      .then((response) => response.json())
      .then((data) => setStatus(`API: ${data.status}`))
      .catch(() => setStatus('API не запущен'));
  }, []);
  return <main><p className="eyebrow">STARTER PROJECT</p><h1>Website Clone Lab</h1><p>Минимальная основа для следующих задач.</p><span className="status">{status}</span></main>;
}

createRoot(document.getElementById('root')).render(<App />);
