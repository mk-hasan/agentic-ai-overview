# Use Case: Human-in-the-Loop — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — creating tickets and other side effects should not run fully unattended.

## Why human-in-the-loop fits

Ticket creation changes systems of record and may notify managers. Pausing the graph before `create_ticket` lets a support lead review summary, category, and priority—approving, editing, or rejecting before the tool executes.

## Example flow

1. Agent troubleshoots VPN issue; FAQ steps insufficient.
2. Agent prepares ticket payload: `{ summary, category: vpn, user email }`.
3. Graph **interrupts** — UI shows pending ticket to the operator.
4. Human approves → graph resumes → `create_ticket` runs → ticket ID returned.
5. Agent tells user: “Ticket INC-1042 opened; expect callback within 4h.”
6. If rejected, agent asks clarifying questions instead of opening a ticket.

## Out of scope

Fully automated low-risk FAQ-only responses without side effects.
