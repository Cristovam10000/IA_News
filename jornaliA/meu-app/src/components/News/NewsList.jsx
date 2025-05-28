// src/components/News/NewsList.jsx
import NewsItem from './NewsItem';

export default function NewsList({ rawMarkdown }) {
  const sections = rawMarkdown
    .split(/^---$/m)
    .map(s => s.trim())
    .filter(Boolean);

  return (
    <div className="news-list">
      {sections.map((sec, i) => (
        <NewsItem key={i} markdown={sec} />
      ))}
    </div>
  );
}
