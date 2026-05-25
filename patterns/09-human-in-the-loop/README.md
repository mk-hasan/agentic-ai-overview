# Human-in-the-Loop (HITL)

## What it is

The agent **pauses for human approval, input, or correction** at defined checkpoints before irreversible or high-risk actions continue.

## When to use it

- Financial transactions, medical advice, production deploys.
- Low trust in model or regulatory requirements.
- Active learning: human corrections improve future runs.

## When not to use it

- Fully automated low-risk flows where latency matters.
- Humans cannot respond within required SLA.

## Related patterns

- [Guardrails](../12-guardrails/) — automated checks before/alongside HITL
- [Evaluator–Optimizer](../08-evaluator-optimizer/) — automated vs. human evaluation
- [Tool Use](../02-tool-use/) — gate dangerous tools behind approval

## Example

See [`example/`](example/) — **LangGraph HITL demo** (IT helpdesk: human approval before ticket creation).

Run from repo root: `python patterns/09-human-in-the-loop/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** Loan approval assistant, content publish workflow, privileged admin actions.
