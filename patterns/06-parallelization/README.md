> **English** | [বাংলা](README.bn.md)

# Parallelization

## What it is

**Independent subtasks run concurrently** (multiple LLM calls, tool calls, or agents), then results are merged. Improves latency for embarrassingly parallel work.

## When to use it

- Summarizing many documents, scoring many candidates.
- Gathering data from multiple APIs at once.
- Fan-out research across sources.

## When not to use it

- Steps depend on each other's outputs sequentially.
- Strict token budgets—parallel calls multiply cost.

## Related patterns

- [Map–Reduce](../14-map-reduce/) — parallel map + reduce merge
- [Orchestrator–Workers](../07-orchestrator-workers/) — workers often run in parallel

## Example

See [`example/`](example/) — **LangGraph parallelization demo** (IT helpdesk: concurrent FAQ + status checks, merged reply).

Run from repo root: `python patterns/06-parallelization/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** Competitive price check, multi-source news brief, batch code review.
