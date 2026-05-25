# Prompt Chaining

## What it is

A **fixed sequence of LLM calls** where each step's output becomes the next step's input. No dynamic branching—predictable pipeline.

## When to use it

- ETL-style text workflows: extract → transform → summarize.
- When each stage has a clear, separate prompt.
- Easier testing and observability per stage.

## When not to use it

- Paths depend on intermediate results (use [Routing](../05-routing/) instead).
- Need parallel speed (use [Parallelization](../06-parallelization/)).

## Related patterns

- [Routing](../05-routing/) — conditional next step
- [Evaluator–Optimizer](../08-evaluator-optimizer/) — loop on quality

## Example

See [`example/`](example/) — **LangGraph prompt-chain demo** (IT helpdesk: extract → classify → draft → format).

Run from repo root: `python patterns/04-prompt-chaining/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** Contract review pipeline, resume screening stages, content moderation.
