# Handoff Example (LangGraph)

Tier-1 IT support escalates complex VPN cases to Tier-2 without losing conversation context.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/13-handoff/example/main.py
python patterns/13-handoff/example/main.py "VPN still drops after all FAQ steps"
```

## What it demonstrates

- Separate Tier-1 and Tier-2 agent nodes with distinct prompts and tools
- Automatic escalation when Tier-1 cannot resolve the issue
- Shared message history passed on handoff for seamless user experience
