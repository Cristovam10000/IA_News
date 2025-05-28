import { useState } from 'react';
import './TopicSelector.css'

const TopicSelector = ({ onFetch }) => {
    const [topic, setTopic] = useState('');

    return (
      <div className='topic-selector'>
        <input
            type='text'
            value={topic}
            onChange={e => setTopic(e.target.value)}
            placeholder="Digite um topico"
            className="topic-input" 
        />
        <button
            onClick={() => onFetch(topic || 'principais notícias do mundo'  )}
            className='topic-button'
        >
            Buscar
        </button>
      </div>
    )
} 

export default TopicSelector;