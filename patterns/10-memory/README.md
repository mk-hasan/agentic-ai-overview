> **English** | [বাংলা](README.bn.md)

# Memory & Context Management

## What it is

**Persist and retrieve** conversation history, user preferences, and session state so agents stay coherent across turns and sessions—short-term (context window) and long-term (store).

## When to use it

- Multi-turn assistants and ongoing projects.
- Personalization without re-explaining context each time.
- Agents that must recall prior decisions.

## When not to use it

- Stateless one-shot transforms.
- Storing sensitive data without retention policy.

## Related patterns

- [RAG](../11-rag/) — memory often backed by vector or document store
- [Planning](../03-planning/) — plans stored as working memory

## Example

See [`example/`](example/) — **LangGraph memory demo** (IT helpdesk: multi-turn chat with checkpointed thread state).

Run from repo root: `python patterns/10-memory/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** Personal shopping assistant, long-running coding session, therapy journaling bot (with privacy controls).
