> **English** | [বাংলা](README.bn.md)

# Routing

## What it is

A **classifier or router** sends each request to the right handler: specialized prompt, agent, or tool set based on intent, metadata, or content.

## When to use it

- Single entry point with diverse request types (support bot, multi-skill assistant).
- Different SLAs or models per route (fast vs. deep).
- Guarded separation of capabilities.

## When not to use it

- All requests need the same processing.
- Routing errors are costlier than a generalist agent.

## Related patterns

- [Orchestrator–Workers](../07-orchestrator-workers/) — router picks which worker agent
- [Handoff](../13-handoff/) — dynamic transfer mid-conversation

## Example

See [`example/`](example/) — **LangGraph routing demo** (IT helpdesk: intent router → VPN / identity / email handlers).

Run from repo root: `python patterns/05-routing/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** Customer support tier-0 router, multi-department internal bot.
