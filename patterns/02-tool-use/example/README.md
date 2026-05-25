> **English** | [বাংলা](README.bn.md)

# Tool Use Example (LangGraph)

IT helpdesk agent with an explicit tool catalog—FAQ search, status checks, and ticket creation via function calling.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/02-tool-use/example/main.py
python patterns/02-tool-use/example/main.py --provider deepseek "I forgot my password"
```

## What it demonstrates

- Declared tool registry bound to the LLM with structured schemas
- Model selects the smallest tool set needed before answering
- Tool results fed back into the agent loop for grounded replies
