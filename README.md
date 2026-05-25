# Agentic AI Overview

A hands-on catalog of **15 agentic AI design patterns**, each with **runnable LangGraph examples** and **three shared real-world scenarios**. Use it to learn how agents are built, how patterns compose, and how to adapt reference code to production systems.

**New here?** Start with [Getting started](docs/getting-started.md) → run [ReAct](patterns/01-react/) → read [single-agent vs multi-agent](docs/architecture/single-vs-multi-agent.md).

---

## What this repo contains

| Layer | What you get |
|-------|----------------|
| **Patterns** (`patterns/01`–`15`) | One folder per design pattern: concept README, use-case template, working `example/` |
| **Scenarios** (`shared/examples/`) | Three domains with mock tools, prompts, and data — swap via `--scenario` |
| **Shared runtime** (`shared/`) | LLM clients, CLI, LangGraph helpers, optional MCP server, scenario registry |
| **Docs** (`docs/`) | Architecture, use-case guides, pattern index, run commands |
| **Tests** (`tests/`) | Unit tests for tools, CLI flags, orchestrator logic, checkpointers |

Every pattern example runs against the **same three scenarios** so you can compare how a pattern behaves in IT support vs e-commerce vs an ML pipeline without rewriting domain logic.

---

## Three use cases (scenarios)

All examples accept `--scenario helpdesk|ecommerce|demand-forecast`:

| Scenario | Domain | Example question | Notable tools |
|----------|--------|------------------|---------------|
| **helpdesk** | Corp IT support | VPN disconnects, password reset | FAQ search, ticket creation, VPN status |
| **ecommerce** | Order support | Where is order #48291? | Order lookup, shipping, returns, refunds |
| **demand-forecast** | ML pipeline (MLDLC) | Train & deploy SKU demand forecast | Load data, train model, MLflow tracking, register model |

Docs: [IT Helpdesk](docs/use-cases/it-helpdesk.md) · [E-commerce](docs/use-cases/ecommerce-order-support.md) · [Demand Forecast](docs/use-cases/demand-forecast.md) · [Run all examples](docs/use-cases/run-all-examples.md)

Shortcut entry points exist under some pattern folders, e.g. `patterns/01-react/example/ecommerce/main.py`.

---

## Quick start

```bash
git clone <repo-url> && cd agentic-ai-overview
python -m venv .venv && source .venv/bin/activate
pip install -e .
cp .env.example .env
# Set OPENAI_API_KEY and/or DEEPSEEK_API_KEY in .env
```

`pip install -e .` installs the `shared` package in editable mode — no `PYTHONPATH` needed.

Run your first agent:

```bash
python patterns/01-react/example/main.py --scenario helpdesk --provider deepseek
python patterns/02-tool-use/example/main.py --scenario ecommerce --provider deepseek
```

Optional extras:

```bash
pip install -e ".[dev]"   # pytest + SQLite checkpointer
pip install -e ".[ml]"    # MLflow (demand-forecast)
pip install -e ".[mcp]"   # MCP tool server (Python 3.10+)
```

Legacy requirement files (`pip install -r requirements.txt`, etc.) also perform editable installs.

---

## Common CLI flags

Every pattern example shares the same CLI (see `shared/examples/cli.py`):

| Flag | Purpose |
|------|---------|
| `--scenario helpdesk\|ecommerce\|demand-forecast` | Pick use case (default: `helpdesk`) |
| `--provider openai\|deepseek` | LLM provider (default from `.env`) |
| `--use-mcp` | Load tools from local MCP server instead of in-process |
| `--no-mlflow` | Mock ML tracking for demand-forecast (no MLflow server) |
| `--stream` / `--no-stream` | Token streaming for chat (default on for helpdesk/ecommerce) |
| `--stream-events` | Stream graph node updates (default on for demand-forecast in 07/15) |

Pattern-specific flags (e.g. `--auto-approve`, `--time-travel` on HITL) are documented in each pattern's `example/README.md`.

---

## 15 design patterns

| # | Pattern | Category | Typical scenario fit |
|---|---------|----------|----------------------|
| 01 | [ReAct](patterns/01-react/) | Core loop | Any tool-using agent |
| 02 | [Tool Use](patterns/02-tool-use/) | Core loop | Explicit tool registry |
| 03 | [Planning](patterns/03-planning/) | Core loop | Multi-step ML pipeline, complex tickets |
| 04 | [Prompt Chaining](patterns/04-prompt-chaining/) | Workflow | Fixed pipelines |
| 05 | [Routing](patterns/05-routing/) | Workflow | VPN vs email vs order intents |
| 06 | [Parallelization](patterns/06-parallelization/) | Workflow | FAQ + status checks at once |
| 07 | [Orchestrator–Workers](patterns/07-orchestrator-workers/) | Workflow | MLDLC specialists (data, modeling, deploy) |
| 08 | [Evaluator–Optimizer](patterns/08-evaluator-optimizer/) | Workflow | Improve answer quality |
| 09 | [Human-in-the-Loop](patterns/09-human-in-the-loop/) | Control | Approve tickets, refunds, model registration |
| 10 | [Memory](patterns/10-memory/) | Control | Multi-turn follow-ups |
| 11 | [RAG](patterns/11-rag/) | Control | FAQ / playbook retrieval |
| 12 | [Guardrails](patterns/12-guardrails/) | Control | PII and policy checks |
| 13 | [Handoff](patterns/13-handoff/) | Advanced | Tier-1 → Tier-2 escalation |
| 14 | [Map–Reduce](patterns/14-map-reduce/) | Advanced | Summarize many incident logs |
| 15 | [Event-Driven](patterns/15-event-driven/) | Advanced | Inbound email / retrain events |

Full index: [patterns/README.md](patterns/README.md) · Glossary: [docs/patterns/glossary.md](docs/patterns/glossary.md)

**Suggested learning order:** 01 ReAct → 02 Tool Use → (11 RAG or 05 Routing) → 09 HITL → 07 Orchestrator–Workers. Details in [Getting started](docs/getting-started.md).

---

## Project structure

```
agentic-ai-overview/
├── patterns/                 # 15 numbered pattern folders
│   └── XX-name/
│       ├── README.md         # What the pattern is, when to use it
│       ├── use-case.md       # Scenario write-up (editable)
│       └── example/          # Runnable graph.py + main.py
├── shared/
│   ├── examples/             # Scenario modules (helpdesk, ecommerce, demand_forecast)
│   │   ├── scenarios.py      # get_scenario() registry
│   │   ├── cli.py            # Shared --scenario, --provider, flags
│   │   ├── tool_provider.py  # Local tools or MCP (--use-mcp)
│   │   └── graphs/           # ReAct builder, worker subgraphs
│   ├── langgraph/            # SQLite checkpointer, streaming, time travel
│   ├── mcp/                  # Optional MCP tool server (stdio)
│   ├── config/               # Paths, defaults, scenario list
│   └── utils/                # LLM clients, env loading
├── docs/
│   ├── getting-started.md
│   ├── architecture/         # LangGraph, MCP, single vs multi-agent
│   ├── patterns/             # Catalog index
│   └── use-cases/            # Per-scenario guides
├── tests/                    # pytest suite
├── templates/pattern-example/  # Scaffold for new examples
├── requirements.txt          # pip install -e . (editable)
├── requirements-dev.txt      # pip install -e ".[dev]"
├── requirements-ml.txt       # pip install -e ".[ml]"
├── requirements-mcp.txt      # pip install -e ".[mcp]"
├── pyproject.toml            # package metadata & optional extras
└── .env.example
```

---

## Framework and runtime features

All examples use **[LangGraph](docs/architecture/langgraph.md)** with **[LangChain Core](https://python.langchain.com/)** messages and tools.

| Feature | Where | Notes |
|---------|-------|-------|
| **OpenAI & DeepSeek** | All examples | `--provider openai\|deepseek` |
| **Chat streaming** | 01, 02 | Token stream for helpdesk/ecommerce |
| **SQLite persistence** | 09, 10 | Checkpoints in `data/checkpoints/` |
| **HITL interrupts** | 09 | Pause before side-effect tools |
| **Time travel** | 09 | `--time-travel` rewinds checkpoints |
| **Worker subgraphs** | 07 | MLDLC workers as compiled subgraphs |
| **Event streaming** | 07, 15 | Pipeline progress via `stream_mode="updates"` |
| **MCP tools** | All (optional) | `--use-mcp` — [MCP docs](docs/architecture/mcp.md) |
| **MLflow tracking** | demand-forecast | On by default; `--no-mlflow` for mock |

Architecture overview: [docs/architecture/overview.md](docs/architecture/overview.md)

---

## Example commands

```bash
# After: pip install -e .

# Chat with streaming (default for helpdesk / ecommerce)
python patterns/01-react/example/main.py --scenario helpdesk --provider deepseek

# Tool catalog + agent
python patterns/02-tool-use/example/main.py --scenario ecommerce

# Human approval before creating a ticket
python patterns/09-human-in-the-loop/example/main.py --scenario helpdesk --auto-approve --time-travel

# Multi-turn memory (SQLite checkpoint)
python patterns/10-memory/example/main.py --scenario helpdesk

# ML pipeline orchestration + event stream
python patterns/07-orchestrator-workers/example/main.py --scenario demand-forecast --no-mlflow

# MLflow UI (when MLflow enabled)
pip install -r requirements-ml.txt && mlflow ui

# MCP tools (Python 3.10+)
pip install -r requirements-mcp.txt
python patterns/01-react/example/main.py --use-mcp --scenario helpdesk
```

---

## Tests

```bash
pip install -e ".[dev]"
pytest
```

45+ unit tests cover scenario tools, CLI flag wiring, orchestrator parsing, worker subgraphs, and checkpointer helpers — no API keys required.

---

## Documentation map

| Doc | Purpose |
|-----|---------|
| [Getting started](docs/getting-started.md) | Learning path and first steps |
| [LangGraph conventions](docs/architecture/langgraph.md) | Graph layout, capabilities, pattern mapping |
| [Single vs multi-agent](docs/architecture/single-vs-multi-agent.md) | Architecture choice |
| [MCP integration](docs/architecture/mcp.md) | Optional MCP tool transport |
| [Run all examples](docs/use-cases/run-all-examples.md) | Copy-paste commands for every pattern |

---

## Contributing / extending

1. Pick a pattern under `patterns/`.
2. Fill in `use-case.md` for your scenario.
3. Extend `example/` or reuse `shared/examples/`.
4. Copy [`templates/pattern-example/`](templates/pattern-example/) to scaffold new variants.

---

## License

See [LICENSE](LICENSE).
