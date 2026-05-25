> **English** | [বাংলা](README.bn.md)

# Tool Use / Function Calling

## What it is

The model selects from a **declared set of tools** (functions, APIs, databases) and returns structured arguments. The runtime executes the tool and feeds results back to the model.

## When to use it

- Grounding answers in live data (weather, CRM, tickets).
- Side effects: send email, create ticket, run query.
- Any ReAct or planner agent that needs structured actions.

## When not to use it

- Pure text generation with no external systems.
- When tool schemas are unstable and hard to maintain.

## Related patterns

- [ReAct](../01-react/) — common execution loop around tool calls
- [Routing](../05-routing/) — different tool sets per route
- [Guardrails](../12-guardrails/) — validate tool inputs/outputs

## Example

See [`example/`](example/) — **LangGraph tool-use demo** (IT helpdesk: explicit FAQ, status, and ticket tools).

Run from repo root: `python patterns/02-tool-use/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** Calendar scheduling, expense approval, inventory lookup.
