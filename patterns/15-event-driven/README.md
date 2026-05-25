# Event-Driven Agents

## What it is

Agents **react to events** (webhooks, queues, schedules, file changes) rather than only synchronous user messages. Long-running, asynchronous, often multi-step workflows.

## When to use it

- Monitoring and alerting pipelines.
- Background processing (nightly reports, sync jobs).
- Integrations with Slack, email, CI, IoT.

## When not to use it

- Simple chat-only interfaces with no external events.
- Event volume exceeds processing capacity without queue design.

## Related patterns

- [Orchestrator–Workers](../07-orchestrator-workers/) — events trigger orchestration
- [Human-in-the-Loop](../09-human-in-the-loop/) — events can await human response
- [Routing](../05-routing/) — route by event type

## Example

See [`example/`](example/) — **LangGraph event-driven demo** (IT helpdesk: inbound support email → async reply).

Run from repo root: `python patterns/15-event-driven/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** GitHub PR review bot, invoice email processor, uptime incident agent.
