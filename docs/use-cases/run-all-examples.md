> **English** | [বাংলা](../bn/use-cases/run-all-examples.md)

# Run all examples

Two scenarios: **helpdesk** (default), **ecommerce**, and **demand-forecast** (ML pipeline / MLDLC). See [use cases README](README.md).

```bash
# Default IT helpdesk
python patterns/01-react/example/main.py --provider openai

# E-commerce order support
python patterns/01-react/example/main.py --scenario ecommerce --provider openai

# Scenario shortcut (same as --scenario helpdesk)
python patterns/01-react/example/ecommerce/main.py --provider deepseek
```

Set `DEFAULT_SCENARIO=ecommerce` in `.env` to change the default.

## All patterns (helpdesk)

| # | Command |
|---|---------|
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

## E-commerce variant

Add `--scenario ecommerce` to any command above, or run from the scenario subfolder:

```bash
python patterns/05-routing/example/ecommerce/main.py --provider openai
```

## Demand forecast (ML pipeline)

Requires ML extras for tracking (optional with `--no-mlflow`):

```bash
pip install -r requirements-ml.txt
python patterns/01-react/example/main.py --scenario demand-forecast --provider openai
python patterns/01-react/example/main.py --scenario demand-forecast --no-mlflow
mlflow ui
```

Add `--provider openai` or `--provider deepseek` to any command.

## MCP tools (optional)

Load the same scenario tools from a local MCP server instead of in-process Python:

```bash
pip install -r requirements-mcp.txt   # Python 3.10+ required
python patterns/01-react/example/main.py --scenario helpdesk --use-mcp --provider openai
```

See [MCP architecture](../architecture/mcp.md).
