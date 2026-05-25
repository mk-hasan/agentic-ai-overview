> [English](../use-cases/run-all-examples.md) | **বাংলা**

# সব উদাহরণ চালান

তিনটি সিনারিও: **helpdesk** (ডিফল্ট), **ecommerce**, **demand-forecast** (ML / MLDLC)। [use cases README](README.md) দেখুন।

```bash
python patterns/01-react/example/main.py --provider openai
python patterns/01-react/example/main.py --scenario ecommerce --provider openai
python patterns/01-react/example/ecommerce/main.py --provider deepseek
```

`.env`-এ `DEFAULT_SCENARIO=ecommerce` দিয়ে ডিফল্ট বদলান।

## সব প্যাটার্ন (helpdesk)

| # | কমান্ড |
|---|--------|
| 01 | `python patterns/01-react/example/main.py` |
| 02 | `python patterns/02-tool-use/example/main.py` |
| 03 | `python patterns/03-planning/example/main.py` |
| 04 | `python patterns/04-prompt-chaining/example/main.py` |
| 05 | `python patterns/05-routing/example/main.py` |
| 06 | `python patterns/06-parallelization/example/main.py` |
| 07 | `python patterns/07-orchestrator-workers/example/main.py` |
| 08 | `python patterns/08-evaluator-optimizer/example/main.py` |
| 09 | `python patterns/09-human-in-the-loop/example/main.py --auto-approve` |
| 10 | `python patterns/10-memory/example/main.py` |
| 11 | `python patterns/11-rag/example/main.py` |
| 12 | `python patterns/12-guardrails/example/main.py` |
| 13 | `python patterns/13-handoff/example/main.py` |
| 14 | `python patterns/14-map-reduce/example/main.py` |
| 15 | `python patterns/15-event-driven/example/main.py` |

## E-commerce

উপরের যেকোনো কমান্ডে `--scenario ecommerce`, অথবা:

```bash
python patterns/05-routing/example/ecommerce/main.py --provider openai
```

## Demand forecast

```bash
pip install -r requirements-ml.txt
python patterns/01-react/example/main.py --scenario demand-forecast --provider openai
python patterns/01-react/example/main.py --scenario demand-forecast --no-mlflow
mlflow ui
```

## MCP (ঐচ্ছিক)

```bash
pip install -r requirements-mcp.txt   # Python 3.10+
python patterns/01-react/example/main.py --scenario helpdesk --use-mcp --provider openai
```

[MCP architecture](../architecture/mcp.md)।
