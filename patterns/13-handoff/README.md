> **English** | [বাংলা](README.bn.md)

# Handoff / Delegation

## What it is

Control **transfers from one agent to another** mid-task—when scope changes, expertise is needed, or the current agent finishes its sub-role.

## When to use it

- Conversational flows that shift domain (sales → support).
- Specialist escalation without restarting context.
- Modular agent teams with clear ownership handover.

## When not to use it

- Single generalist agent suffices.
- Handoff loses critical context without good state passing.

## Related patterns

- [Routing](../05-routing/) — handoff at start vs. mid-flight
- [Orchestrator–Workers](../07-orchestrator-workers/) — orchestrator assigns; handoff is peer transfer

## Example

See [`example/`](example/) — **LangGraph handoff demo** (IT helpdesk: Tier-1 → Tier-2 escalation with shared context).

Run from repo root: `python patterns/13-handoff/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** Sales-to-support escalation, nurse-to-doctor handoff simulation, tier-1 to tier-2 IT.
