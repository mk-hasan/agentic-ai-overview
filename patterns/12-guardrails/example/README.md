# Guardrails Example (LangGraph)

Input policy checks block PII and unsafe content before the IT helpdesk agent runs.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/12-guardrails/example/main.py
python patterns/12-guardrails/example/main.py "My VPN keeps disconnecting"
```

## What it demonstrates

- Pre-agent guardrail node validates user input (e.g. SSN detection)
- Blocked requests return a safe refusal without calling the LLM
- Normal VPN questions pass through to the standard helpdesk agent
