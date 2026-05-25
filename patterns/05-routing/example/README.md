# Routing Example (LangGraph)

Single helpdesk entry point that classifies intent and dispatches to VPN, identity, or email specialist handlers.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/05-routing/example/main.py
python patterns/05-routing/example/main.py "I need to reset my password and MFA"
```

## What it demonstrates

- Router node classifies user intent before any specialist runs
- Separate handler subgraphs with domain-focused prompts and tools
- Route label exposed in output for logging and analytics
