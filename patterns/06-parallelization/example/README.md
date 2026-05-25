# Parallelization Example (LangGraph)

Concurrent FAQ search and service-status checks merged into one IT helpdesk reply.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/06-parallelization/example/main.py
python patterns/06-parallelization/example/main.py "VPN drops and Outlook is slow"
```

## What it demonstrates

- Fan-out to parallel branches (FAQ, VPN status, email status)
- Merge node waits for all branches before synthesizing a response
- Lower latency vs. sequential tool rounds for independent lookups
