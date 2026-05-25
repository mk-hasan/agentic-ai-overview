# Orchestrator–Workers Example (LangGraph)

Supervisor agent delegates VPN, identity, and email work to specialist worker agents, then synthesizes one answer.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/07-orchestrator-workers/example/main.py
python patterns/07-orchestrator-workers/example/main.py "VPN fails after password reset"
```

## What it demonstrates

- Central orchestrator chooses which specialist worker runs next
- Each worker has its own system prompt and tool subset
- Orchestrator merges worker outputs into a single user-facing response
