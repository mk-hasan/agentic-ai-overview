"""Simple retrieval for e-commerce policy markdown files."""

from pathlib import Path

from shared.examples.ecommerce.policies import POLICY_ENTRIES

DATA_DIR = Path(__file__).resolve().parent / "data"


def _score(query: str, text: str, tags: list[str]) -> int:
    query_lower = query.lower()
    score = 0
    for word in query_lower.split():
        if len(word) < 3:
            continue
        if word in text.lower():
            score += 2
        if any(word in tag for tag in tags):
            score += 3
    return score


def retrieve_policy_chunks(query: str, top_k: int = 3) -> list[dict]:
    ranked = []
    for key, entry in POLICY_ENTRIES.items():
        score = _score(query, entry["text"], entry["tags"])
        if score > 0:
            ranked.append(
                {
                    "id": key,
                    "title": entry["title"],
                    "text": entry["text"],
                    "score": score,
                }
            )
    ranked.sort(key=lambda item: item["score"], reverse=True)
    return ranked[:top_k]


def retrieve_from_markdown(query: str, top_k: int = 3) -> list[dict]:
    kb_dir = DATA_DIR / "kb"
    if not kb_dir.exists():
        return retrieve_policy_chunks(query, top_k=top_k)

    ranked = []
    for path in kb_dir.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        title = path.stem.replace("-", " ").title()
        tags = path.stem.split("-")
        score = _score(query, text, tags)
        if score > 0:
            ranked.append(
                {"id": path.stem, "title": title, "text": text.strip(), "score": score}
            )
    ranked.sort(key=lambda item: item["score"], reverse=True)
    return ranked[:top_k] if ranked else retrieve_policy_chunks(query, top_k=top_k)


def format_retrieved_context(chunks: list[dict]) -> str:
    if not chunks:
        return "No relevant policy entries found."
    parts = [f"### {c['title']}\n{c['text']}" for c in chunks]
    return "\n\n".join(parts)
