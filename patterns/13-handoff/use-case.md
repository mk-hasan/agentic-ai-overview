# Use Case: Handoff — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — Tier-1 resolves common issues; complex cases escalate to Tier-2 without losing context.

## Why handoff fits

Early triage should stay fast and scoped. When FAQ and status checks fail or the case needs deeper VPN diagnostics, control transfers from Tier-1 to Tier-2 agent—same thread, new specialist prompt and tools—instead of restarting the conversation.

## Example flow

1. Tier-1 agent searches FAQ and checks VPN status for disconnect report.
2. User confirms steps failed; issue persists on corp network only.
3. Tier-1 invokes handoff → Tier-2 agent receives full message history.
4. Tier-2 runs advanced checks, gathers logs, opens priority ticket.
5. User sees seamless transition: “Escalating to advanced support…”
6. Final answer from Tier-2 includes ticket ID and next SLA window.

## Out of scope

Initial intent routing at first message (see Routing) and orchestrator worker pools.
