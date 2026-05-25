> **English** | [বাংলা](use-case.bn.md)

# Use Case: Event-Driven — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — employees email `support@corp.example.com`; the agent reacts asynchronously instead of waiting in chat.

## Why event-driven fits

Not every request arrives via live chat. Inbound email events (from, subject, body) trigger a workflow: parse the message, classify urgency, draft a reply or internal ticket—decoupled from user presence and suitable for queues or webhooks.

## Example flow

1. Email event arrives: `{ from: alex@corp, subject: "VPN again", body: "..." }`.
2. Ingest node normalizes event → user request string for the agent.
3. Agent classifies VPN issue, searches FAQ, checks status asynchronously.
4. Agent drafts reply email with steps and optional ticket creation.
5. Response node emits `{ to, subject, body }` for mailer or ticketing integration.
6. Employee receives email reply minutes later without opening the portal.

## Out of scope

Synchronous chat UX and human interrupt approval mid-flight.
