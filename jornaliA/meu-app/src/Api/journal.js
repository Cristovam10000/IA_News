export async function fetchJournal(topic) {
    const resp = await fetch(
        `http://127.0.0.1:8000/jornal?topic=${encodeURIComponent(topic)}`
);
    if (!resp.ok) throw new Error(`Status ${resp.status}`);
    const { markdown } = await resp.json();
    return markdown;
}