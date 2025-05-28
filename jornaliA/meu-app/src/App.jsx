import { useState } from "react";
import { fetchJournal } from "./Api/journal";
import Button from "./components/Button";
import TopicSelector from './components/TopicSelector';
import {NewsList} from './components/News';
import './index.css';


function App() {
  const [markdown, setMarkdown] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleFetch = async topic => {
    setLoading(true);
    setError('');

    try {
      const md = await fetchJournal(topic);
      setMarkdown(md);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

    return (
      <div className="app-container">
      <h1>IA Jornal</h1>
      <TopicSelector onFetch={handleFetch} />

      {loading && <p>Carregando notícias…</p>}
      {error   && <p className="error">Erro: {error}</p>}
      {!loading && !error && markdown && (
        <NewsList rawMarkdown={markdown} />
      )}
    </div>
    );
}

export default App;