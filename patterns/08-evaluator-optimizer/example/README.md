> **English** | [বাংলা](README.bn.md)

# Evaluator–Optimizer Example (LangGraph)

Draft helpdesk reply, score it against quality criteria, and revise until the score passes a threshold.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/08-evaluator-optimizer/example/main.py
python patterns/08-evaluator-optimizer/example/main.py "VPN keeps disconnecting"
```

## What it demonstrates

- Generator and evaluator nodes in a reflection loop
- Score and feedback drive revision rounds until quality threshold met
- Final optimized reply with round count and score logged
