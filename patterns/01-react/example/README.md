# ReAct Example (LangGraph)

Minimal **ReAct** loop using LangGraph: an IT helpdesk agent searches a FAQ, then opens a ticket if needed.

## Graph

```
START → agent → (tool calls?) → tools → agent → … → END
         ↑__________________________|
              observe & reason again
```

- **agent** — LLM reasons and optionally requests tools
- **tools** — runs `search_faq` / `create_ticket`, returns observations
- Loop continues until the model responds without tool calls

## Prerequisites

- Python 3.11+
- **OpenAI** and/or **DeepSeek** API key in `.env`

## Setup

From the **repo root**:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env — set OPENAI_API_KEY and/or DEEPSEEK_API_KEY
```

See [LangGraph conventions](../../../docs/architecture/langgraph.md) for shared helpers.

## Run

```bash
# Default provider (DEFAULT_PROVIDER in .env, usually openai)
python patterns/01-react/example/main.py

# OpenAI explicitly
python patterns/01-react/example/main.py --provider openai

# DeepSeek
python patterns/01-react/example/main.py --provider deepseek

# Tools via MCP subprocess (optional; Python 3.10+, pip install -r requirements-mcp.txt)
python patterns/01-react/example/main.py --use-mcp --provider openai

# Custom question
python patterns/01-react/example/main.py --provider deepseek "I forgot my password"
```

## Files

| File | Purpose |
|------|---------|
| `main.py` | Entry point — `--provider`, invokes graph |
| `graph.py` | `StateGraph` — agent ↔ tools ReAct loop |
| `tools.py` | Mock FAQ search and ticket creation |

## Next steps

1. Replace mock tools in `tools.py` with real APIs.
2. Document your scenario in [`../use-case.md`](../use-case.md).
3. Add RAG ([`11-rag`](../../11-rag/)) if FAQ lives in documents instead of a dict.
