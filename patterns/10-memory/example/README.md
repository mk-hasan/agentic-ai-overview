> **English** | [বাংলা](README.bn.md)

# Memory Example (LangGraph)

Multi-turn IT helpdesk chat with checkpointed conversation state across two turns on the same thread.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/10-memory/example/main.py
python patterns/10-memory/example/main.py --provider deepseek
```

## What it demonstrates

- LangGraph checkpointer retains messages under a fixed `thread_id`
- Turn 2 follow-up reuses prior VPN context without re-explaining
- Same ReAct tools as helpdesk, with session continuity as the focus
