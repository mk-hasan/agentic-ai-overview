> **English** | [বাংলা](README.bn.md)

# Planning & Task Decomposition

## What it is

Before acting, the agent **breaks a goal into subtasks** (a plan), then executes them in order—often with replanning when steps fail or new information appears.

## When to use it

- Multi-step projects (report generation, migration checklist).
- Tasks where order and dependencies matter.
- Reducing wasted tool calls via upfront structure.

## When not to use it

- Simple one-tool lookups.
- Highly reactive environments where plans go stale quickly.

## Related patterns

- [ReAct](../01-react/) — execute individual plan steps
- [Orchestrator–Workers](../07-orchestrator-workers/) — assign subtasks to workers
- [Map–Reduce](../14-map-reduce/) — parallel subtasks with merge step

## Example

See [`example/`](example/) — **LangGraph planning demo** (IT helpdesk: plan steps, then execute with tools).

Run from repo root: `python patterns/03-planning/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** Trip planning, software release checklist, onboarding workflow.
