> **English** | [বাংলা](../bn/patterns/README.md)

# Agentic AI Design Patterns

A catalog of common patterns for building autonomous and semi-autonomous AI agents. Each pattern has a dedicated folder under [`patterns/`](../../patterns/) with space for a real-life use case and a runnable example.

**Architecture:** [Single-agent vs multi-agent](../architecture/single-vs-multi-agent.md) — when to use one agent vs a coordinated team.

## Pattern Index

| # | Pattern | Category | Folder |
|---|---------|----------|--------|
| 01 | [ReAct (Reason + Act)](../../patterns/01-react/) | Core loop | `patterns/01-react/` |
| 02 | [Tool Use / Function Calling](../../patterns/02-tool-use/) | Core loop | `patterns/02-tool-use/` |
| 03 | [Planning & Task Decomposition](../../patterns/03-planning/) | Core loop | `patterns/03-planning/` |
| 04 | [Prompt Chaining](../../patterns/04-prompt-chaining/) | Workflow | `patterns/04-prompt-chaining/` |
| 05 | [Routing](../../patterns/05-routing/) | Workflow | `patterns/05-routing/` |
| 06 | [Parallelization](../../patterns/06-parallelization/) | Workflow | `patterns/06-parallelization/` |
| 07 | [Orchestrator–Workers (Multi-Agent)](../../patterns/07-orchestrator-workers/) | Workflow | `patterns/07-orchestrator-workers/` |
| 08 | [Evaluator–Optimizer (Reflection)](../../patterns/08-evaluator-optimizer/) | Workflow | `patterns/08-evaluator-optimizer/` |
| 09 | [Human-in-the-Loop (HITL)](../../patterns/09-human-in-the-loop/) | Control | `patterns/09-human-in-the-loop/` |
| 10 | [Memory & Context Management](../../patterns/10-memory/) | Control | `patterns/10-memory/` |
| 11 | [Retrieval-Augmented Generation (RAG)](../../patterns/11-rag/) | Control | `patterns/11-rag/` |
| 12 | [Guardrails & Safety](../../patterns/12-guardrails/) | Control | `patterns/12-guardrails/` |
| 13 | [Handoff / Delegation](../../patterns/13-handoff/) | Advanced | `patterns/13-handoff/` |
| 14 | [Map–Reduce](../../patterns/14-map-reduce/) | Advanced | `patterns/14-map-reduce/` |
| 15 | [Event-Driven Agents](../../patterns/15-event-driven/) | Advanced | `patterns/15-event-driven/` |

## Categories

- **Core loop** — How a single agent thinks, decides, and acts.
- **Workflow** — How multiple steps or agents are composed into a pipeline.
- **Control** — Human oversight, memory, retrieval, and safety boundaries.
- **Advanced** — Delegation, scaling, and reactive architectures.

## Adding a New Example

1. Copy [`templates/pattern-example/`](../../templates/pattern-example/) or use an existing pattern folder.
2. Fill in `use-case.md` with the real-life scenario (problem, actors, constraints, success criteria).
3. Implement the example under `example/` and document how to run it in that folder's README.
4. Link your example from the pattern's main `README.md`.

See [`docs/architecture/overview.md`](../architecture/overview.md) for how folders relate to each other.

**Getting started:** [docs/getting-started.md](../getting-started.md) — recommended first pattern is **01 ReAct**, then **02 Tool Use**.

**Shared scenario:** [Corp IT Helpdesk](../use-cases/it-helpdesk.md) — all 15 examples. [Run commands](../use-cases/run-all-examples.md).
