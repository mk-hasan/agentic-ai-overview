> **English** | [বাংলা](README.bn.md)

# Planning Example (LangGraph)

IT helpdesk agent that decomposes a user request into a step plan, then executes each step with tools before synthesizing a final reply.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/03-planning/example/main.py
python patterns/03-planning/example/main.py --provider openai "VPN and Outlook both failing"
```

## What it demonstrates

- Separate plan and execute nodes in a LangGraph workflow
- Ordered troubleshooting steps (FAQ → status → ticket) instead of ad-hoc tool calls
- Plan state tracked across steps with a final synthesis message
