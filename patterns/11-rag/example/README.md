> **English** | [বাংলা](README.bn.md)

# RAG Example (LangGraph)

Retrieve relevant chunks from markdown KB files, then answer IT helpdesk questions with grounded context and tools.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/11-rag/example/main.py
python patterns/11-rag/example/main.py "VPN keeps disconnecting every few minutes"
```

## What it demonstrates

- Retrieval step loads snippets from `shared/examples/helpdesk/data/kb/`
- Retrieved context injected before the agent reasoning step
- Reduces hallucinated runbook steps by grounding on internal docs
