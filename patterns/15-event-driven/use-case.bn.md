> [English](use-case.md) | **বাংলা**

# Use Case: Event-Driven — Corp IT Helpdesk

শেয়ার্ড সিনারিও: [Corp IT Helpdesk](../../docs/bn/use-cases/it-helpdesk.md) — VPN, password reset, Outlook issues।

## কেন Event-Driven মানায়

Inbound support email webhook — async process, reply generation, optional ticket।

## উদাহরণ ফ্লো

1. Email event payload arrives।
2. Event handler subgraph triggered।
3. Classify + retrieve + draft reply।
4. Optional HITL/ticket side effects।
5. Async completion / notification।

## এই সিনারিওতে নয়

Sync chat-only, no external events।
