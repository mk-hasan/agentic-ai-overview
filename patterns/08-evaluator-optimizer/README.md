# Evaluator–Optimizer (Reflection)

## What it is

Generate a draft, **evaluate** it against criteria (another LLM call, rules, or tests), then **revise** in a loop until quality thresholds are met or max iterations reached.

## When to use it

- High-quality writing, code, or analysis where first drafts fail often.
- Measurable rubrics (style guide, test suite, policy checklist).
- Self-correction without human in every loop.

## When not to use it

- Latency-sensitive paths.
- Evaluation is subjective and rubrics are weak (loops may not converge).

## Related patterns

- [Human-in-the-Loop](../09-human-in-the-loop/) — human as evaluator
- [Guardrails](../12-guardrails/) — hard rules vs. soft critique
- [ReAct](../01-react/) — reflection can follow each action

## Example

See [`example/`](example/) — **LangGraph evaluator–optimizer demo** (IT helpdesk: draft, score, revise until quality passes).

Run from repo root: `python patterns/08-evaluator-optimizer/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** Email tone refinement, SQL query fix-up, marketing copy compliance.
