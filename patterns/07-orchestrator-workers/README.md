# Orchestrator–Workers (Multi-Agent)

## What it is

A **central orchestrator** decomposes work and delegates to **specialist worker agents**, each with its own tools and prompts. The orchestrator synthesizes outputs.

## When to use it

- Complex domains needing distinct expertise (legal + finance + engineering).
- Clear role boundaries and audit trails per specialist.
- Tasks too large for one monolithic prompt.

## When not to use it

- Overhead of coordination exceeds benefit.
- Workers would duplicate the same capabilities.

## Related patterns

- [Planning](../03-planning/) — orchestrator often produces the plan
- [Handoff](../13-handoff/) — workers pass control to each other
- [Parallelization](../06-parallelization/) — workers may run concurrently

## Example

See [`example/`](example/) — **LangGraph orchestrator–workers demo** (IT helpdesk: supervisor + VPN / identity / email specialists).

Run from repo root: `python patterns/07-orchestrator-workers/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** Software feature delivery team, incident response war room, research lab.
