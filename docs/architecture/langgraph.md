> **English** | [বাংলা](../bn/architecture/langgraph.md)

# LangGraph

All runnable examples in this repo use **[LangGraph](https://langchain-ai.github.io/langgraph/)** as the default agent framework.

## Why LangGraph here

- **Graph-based flows** map directly to design patterns (ReAct loop, routing, multi-agent).
- **Shared state** (`MessagesState`, custom state) supports memory and planning.
- **Checkpoints & interrupts** support human-in-the-loop and persistence.
- **Prebuilt components** (`ToolNode`, `tools_condition`, supervisors) speed up examples without hiding the pattern.

LangChain Core provides messages and tools; you do not need the full LangChain stack.

## Standard example layout

```
patterns/XX-name/example/
├── main.py          # Entry point (adds repo root to sys.path)
├── graph.py         # StateGraph definition
├── tools.py         # @tool definitions (when applicable)
├── nodes.py         # Optional: split node logic for larger graphs
├── state.py         # Optional: custom TypedDict state
├── requirements.txt # Optional: pin extra deps beyond repo root
└── README.md        # How to run
```

Shared setup lives in [`shared/`](../../shared/):

| Module | Purpose |
|--------|---------|
| `shared/utils/env.py` | Load `.env` from repo root |
| `shared/utils/llm.py` | `get_openai_chat_model()`, `get_deepseek_chat_model()`, `get_chat_model(provider=...)` |
| `shared/utils/cli.py` | `--provider openai\|deepseek` flag for example CLIs |
| `shared/config/settings.py` | Paths, default models, provider names |

## Install (once per environment)

From the repo root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
# Set OPENAI_API_KEY and/or DEEPSEEK_API_KEY in .env
```

Optional: `pip install -e ".[dev]"` for pytest and SQLite checkpointer.

## LLM providers

Every example supports **two providers**:

| Provider | Helper | Env vars |
|----------|--------|----------|
| OpenAI | `get_openai_chat_model()` | `OPENAI_API_KEY`, `OPENAI_MODEL`, optional `OPENAI_BASE_URL` |
| DeepSeek | `get_deepseek_chat_model()` | `DEEPSEEK_API_KEY`, `DEEPSEEK_MODEL`, `DEEPSEEK_BASE_URL` |

Use `get_chat_model(provider="openai")` or `get_chat_model(provider="deepseek")`, or pass `--provider` on the CLI:

```python
from shared.utils.llm import get_chat_model

model = get_chat_model(provider="deepseek").bind_tools(tools)
```

```bash
python patterns/01-react/example/main.py --provider deepseek "How do I reset my password?"
python patterns/01-react/example/main.py --provider openai
```

Set `DEFAULT_PROVIDER=deepseek` in `.env` to change the default without passing `--provider`.

## Scenarios

Every example supports two use cases via `--scenario`:

| Scenario | Description |
|----------|-------------|
| `helpdesk` (default) | Corp IT support — VPN, password, email |
| `ecommerce` | Order #48291 — tracking, shipping, returns, refunds |
| `demand-forecast` | SKU demand forecasting — full MLDLC pipeline |

```bash
python patterns/01-react/example/main.py --scenario ecommerce --provider openai
python patterns/01-react/example/ecommerce/main.py   # shortcut
```

Shared modules: `shared/examples/helpdesk/`, `shared/examples/ecommerce/`, registry in `shared/examples/scenarios.py`.

See [use cases](../../use-cases/README.md).

## Run an example

```bash
python patterns/01-react/example/main.py
python patterns/01-react/example/main.py --provider deepseek "How do I reset my password?"
python patterns/01-react/example/main.py --provider openai
```

## Pattern → LangGraph mapping

| Pattern | LangGraph approach |
|---------|-------------------|
| 01 ReAct | Agent node + `ToolNode` loop via `tools_condition` |
| 02 Tool Use | `@tool` + `ToolNode` |
| 03 Planning | Plan node → subgraph or sequential nodes |
| 04 Prompt Chaining | Linear chain of nodes |
| 05 Routing | `add_conditional_edges` on classifier output |
| 06 Parallelization | Parallel branches / `Send` API |
| 07 Orchestrator–Workers | Supervisor graph + worker subgraphs |
| 08 Evaluator–Optimizer | Generate node ↔ evaluate node loop |
| 09 Human-in-the-Loop | `interrupt()` + SQLite checkpointer + time travel |
| 10 Memory | SQLite checkpointer + `thread_id` |
| 11 RAG | Retrieve node before agent node |
| 12 Guardrails | Pre/post nodes or middleware on edges |
| 13 Handoff | Command-based routing to another agent node |
| 14 Map–Reduce | Map `Send` + reduce node |
| 15 Event-Driven | Nested handler subgraph + `graph.stream(..., stream_mode="updates")` |

## LangGraph capabilities in this repo

| Capability | Patterns | How |
|------------|----------|-----|
| **Persistence** | 09, 10 | SQLite checkpointer — `shared/langgraph/checkpointer.py` → `data/checkpoints/langgraph.db` |
| **Interrupts** | 09 | `interrupt()` before side-effect tools; resume with `Command(resume=...)` |
| **Time travel** | 09 | `--time-travel` lists `get_state_history()` and forks with `update_state()` |
| **Memory** | 10 | Same SQLite checkpointer; multi-turn via `thread_id` in config |
| **Subgraphs** | 07, 15 | Worker ReAct subgraphs (`shared/examples/graphs/worker_subgraph.py`); event handler subgraph |
| **Streaming (chat)** | 01, 02 | Default for helpdesk/ecommerce — `stream_mode="messages"`; `--no-stream` to disable |
| **Event streaming** | 07, 15 | Default for demand-forecast — `stream_mode="updates"`; `--stream-events` elsewhere |

Install SQLite persistence: `pip install -e ".[dev]"`

```bash
# Chat streaming (helpdesk / ecommerce)
python patterns/01-react/example/main.py --scenario helpdesk --provider deepseek

# HITL + time travel + SQLite
python patterns/09-human-in-the-loop/example/main.py --auto-approve --time-travel

# Orchestrator subgraphs + pipeline events (demand-forecast)
python patterns/07-orchestrator-workers/example/main.py --scenario demand-forecast --no-mlflow

# Event-driven nested subgraph + events
python patterns/15-event-driven/example/main.py --scenario demand-forecast
```

Not yet demonstrated: durable execution (LangGraph Platform), fault-tolerance retries, token streaming on ML pipeline graphs.

## Starter implementation

The first working example is [`patterns/01-react/example/`](../../patterns/01-react/example/) — a minimal IT helpdesk ReAct graph.
