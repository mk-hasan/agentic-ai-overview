> **English** | [বাংলা](README.bn.md)

# ReAct (Reason + Act)

## What it is

An agent alternates between **reasoning** (planning the next step in natural language) and **acting** (calling tools or APIs), then **observes** the result and repeats until the task is done.

## When to use it

- Tasks that require multiple steps with external feedback (search, code run, API calls).
- When you need interpretable step-by-step behavior.
- Default loop for many tool-using agents.

## When not to use it

- Single-shot Q&A with no tools.
- Strict latency budgets where planning overhead is too costly.

## Structure

```
Thought → Action → Observation → Thought → … → Final Answer
```

## Related patterns

- [Tool Use](../02-tool-use/) — actions are usually tool calls
- [Planning](../03-planning/) — explicit plan before the ReAct loop
- [Evaluator–Optimizer](../08-evaluator-optimizer/) — critique after each cycle

## Example

See [`example/`](example/) — **LangGraph ReAct starter** (IT helpdesk: FAQ search + ticket tool).

Run from repo root: `python patterns/01-react/example/main.py`

## Real-life use case

Corp IT Helpdesk scenario in [`use-case.md`](use-case.md) — links to the shared [scenario doc](../../docs/use-cases/it-helpdesk.md).
