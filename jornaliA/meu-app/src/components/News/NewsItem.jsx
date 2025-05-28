// src/components/News/NewsItem.jsx
import ReactMarkdown from 'react-markdown';

export default function NewsItem({ markdown }) {
  return (
    <article className="news-item">
      <ReactMarkdown>{markdown}</ReactMarkdown>
    </article>
  );
}
