# Human-in-the-Loop Example (LangGraph)

IT helpdesk agent pauses for human approval before creating a support ticket.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/09-human-in-the-loop/example/main.py
python patterns/09-human-in-the-loop/example/main.py --auto-approve
python patterns/09-human-in-the-loop/example/main.py "VPN keeps disconnecting"
```

## What it demonstrates

- Graph interrupt before irreversible `create_ticket` side effect
- Interactive prompt (or `--auto-approve`) resumes the graph with a decision
- Checkpointed thread state so approval flow survives the pause
