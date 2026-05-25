# Guardrails & Safety

## What it is

**Automated checks** on inputs, outputs, and tool calls: policy filters, PII redaction, schema validation, allowlists, and refusal rules—before and after model steps.

## When to use it

- Regulated industries and customer-facing agents.
- Agents with side-effecting tools.
- Defense in depth alongside HITL.

## When not to use it

- Internal prototypes with trusted users only (still recommended minimally).

## Related patterns

- [Human-in-the-Loop](../09-human-in-the-loop/) — human override when guardrails uncertain
- [Tool Use](../02-tool-use/) — validate tool args and results
- [Routing](../05-routing/) — block or redirect unsafe intents

## Example

See [`example/`](example/) — **LangGraph guardrails demo** (IT helpdesk: block PII before the agent runs).

Run from repo root: `python patterns/12-guardrails/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** Healthcare triage boundaries, PII-safe support bot, payment amount limits.
