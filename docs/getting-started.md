# Getting Started

Recommended order for reading docs and building your **first examples**. You do not need all 15 patterns before shipping anything useful—start small, then layer patterns as your use case demands.

## Before you code (15 minutes)

1. [Single-agent vs multi-agent](architecture/single-vs-multi-agent.md) — pick your architecture (default: **single-agent**).
2. [Pattern index](patterns/README.md) — skim categories so you know what exists.
3. Install the project in editable mode and copy env template:
   ```bash
   pip install -e .
   cp .env.example .env
   ```
   This makes `shared` importable from any pattern example without `PYTHONPATH`.
4. Read [LangGraph conventions](architecture/langgraph.md) — all examples use LangGraph.

## Your first pattern: start here

### 1. [ReAct](../patterns/01-react/) — **always first**

ReAct is the default loop for tool-using agents: **think → act → observe → repeat**.

Why first:
- Every other single-agent pattern builds on or wraps this loop.
- Easiest to debug (each step is visible).
- Matches how most frameworks (LangChain, LangGraph, OpenAI Agents, etc.) structure agents.

**First example idea:** an IT helpdesk bot that searches a FAQ and opens a ticket—agent reasons about the issue, calls search, then calls a ticket tool.

Work in:
- `patterns/01-react/use-case.md` — write the scenario
- `patterns/01-react/example/` — **starter already implemented** (LangGraph ReAct + mock IT tools)

Run it:

```bash
python patterns/01-react/example/main.py --provider openai
python patterns/01-react/example/main.py --provider deepseek
```

---

### 2. [Tool Use](../patterns/02-tool-use/) — **second (often same example as ReAct)**

ReAct without tools is just chain-of-thought. Tool use is how the agent **does** things.

Implement tools in the same ReAct example, or split a second minimal example with one tool (e.g. calculator, mock API).

**Do not skip this** if your use case touches real data or side effects.

---

### 3. Pick one branch based on your use case

| If your scenario needs… | Next pattern | Folder |
|-------------------------|--------------|--------|
| Company docs / policies | RAG | [11-rag](../patterns/11-rag/) |
| Many steps with a plan | Planning | [03-planning](../patterns/03-planning/) |
| Better output quality | Evaluator–Optimizer | [08-evaluator-optimizer](../patterns/08-evaluator-optimizer/) |
| Fixed pipeline (no dynamic loop) | Prompt Chaining | [04-prompt-chaining](../patterns/04-prompt-chaining/) |
| Different intents → different handlers | Routing | [05-routing](../patterns/05-routing/) |
| Safety / compliance | Guardrails | [12-guardrails](../patterns/12-guardrails/) |
| Approval before action | Human-in-the-Loop | [09-human-in-the-loop](../patterns/09-human-in-the-loop/) |

---

### 4. Multi-agent — **only after a working single-agent example**

When one agent’s prompt and tools become too large, or you need clear roles (researcher vs writer vs reviewer):

1. [Orchestrator–Workers](../patterns/07-orchestrator-workers/)
2. [Handoff](../patterns/13-handoff/) — if control passes mid-conversation

---

## Suggested learning path (full repo tour)

Build or study examples in this order:

```
Phase 1 — Foundation (single-agent)
  01 ReAct  →  02 Tool Use  →  03 Planning

Phase 2 — Quality & knowledge
  11 RAG  →  08 Evaluator–Optimizer  →  12 Guardrails

Phase 3 — Workflow composition
  04 Prompt Chaining  →  05 Routing  →  06 Parallelization

Phase 4 — Multi-agent & scale
  07 Orchestrator–Workers  →  13 Handoff  →  14 Map–Reduce

Phase 5 — Production shapes
  09 Human-in-the-Loop  →  10 Memory  →  15 Event-Driven
```

Phases 2–5 can overlap; order within a phase is flexible.

---

## Minimal first project (recommended)

One end-to-end example that combines the essentials:

| Step | What to build |
|------|----------------|
| 1 | Choose one real use case (support bot, research assistant, ops checklist) |
| 2 | Write `use-case.md` under `patterns/01-react/` |
| 3 | Implement ReAct loop + 2–3 tools in `patterns/01-react/example/` |
| 4 | Add RAG (`11-rag`) if answers must come from your documents |
| 5 | Add guardrails (`12-guardrails`) before any destructive tool |

That gives you a credible single-agent demo before touching multi-agent.

---

## Per-pattern workflow (every time)

1. Read the pattern `README.md`
2. Fill in `use-case.md` (problem, actors, success criteria)
3. Implement under `example/`
4. Document run steps in `example/README.md`
5. Pull shared code into `shared/` only when a second example needs it

Copy [`templates/pattern-example/`](../templates/pattern-example/) if you want a blank scaffold.

---

## Quick decision: “Which folder do I open today?”

| You are… | Open |
|----------|------|
| Brand new to agentic AI | [patterns/01-react/](../patterns/01-react/) |
| Have ReAct, need external APIs | [patterns/02-tool-use/](../patterns/02-tool-use/) |
| Have tools, need internal docs | [patterns/11-rag/](../patterns/11-rag/) |
| Ready for multiple specialist agents | [patterns/07-orchestrator-workers/](../patterns/07-orchestrator-workers/) |
| Unsure | [patterns/01-react/](../patterns/01-react/) |
