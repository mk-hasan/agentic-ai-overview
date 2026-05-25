> **English** | [বাংলা](README.bn.md)

# Prompt Chaining Example (LangGraph)

Linear IT helpdesk pipeline: extract issue → classify category → draft reply → format for the user.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/04-prompt-chaining/example/main.py
python patterns/04-prompt-chaining/example/main.py "My VPN keeps disconnecting"
```

## What it demonstrates

- Fixed sequence of LLM stages with no dynamic branching
- Each stage’s output stored in graph state for the next prompt
- Observable intermediate fields (`extracted_issue`, `category`, `final_response`)
