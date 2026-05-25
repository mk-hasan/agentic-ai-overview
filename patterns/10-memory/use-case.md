# Use Case: Memory — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — employees return in the same thread with follow-ups instead of repeating context.

## Why memory fits

Support is multi-turn: yesterday’s VPN fix may relate to today’s Outlook error on the same laptop. Checkpointed conversation state lets the agent recall prior steps, ticket IDs, and user details without re-asking or contradicting earlier advice.

## Example flow

1. **Turn 1:** User reports VPN disconnects → agent gives FAQ steps; no ticket yet.
2. Session checkpoint stores messages and resolved steps under `thread_id`.
3. **Turn 2:** User: “VPN worked briefly; now Outlook fails too.”
4. Agent recalls prior VPN context and same laptop/network.
5. Agent skips redundant reboot advice; focuses on linked Outlook cache steps.
6. User gets continuity—“since the VPN fix was temporary, try…”—without re-explaining.

## Out of scope

Long-term cross-session user profiles stored in external CRM.
