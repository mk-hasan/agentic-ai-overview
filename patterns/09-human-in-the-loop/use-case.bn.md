> [English](use-case.md) | **বাংলা**

# Use Case: Human-in-the-Loop — Corp IT Helpdesk

শেয়ার্ড সিনারিও: [Corp IT Helpdesk](../../docs/bn/use-cases/it-helpdesk.md) — VPN, password reset, Outlook issues।

## কেন Human-in-the-Loop মানায়

Ticket creation, privileged actions — irreversible side effect-এর আগে manager approve।

## উদাহরণ ফ্লো

1. Agent decides ticket needed।
2. Graph interrupt before `create_ticket`।
3. Human approve/reject/edit।
4. Resume with `Command(resume=...)`।
5. Ticket created or alternative path।

## এই সিনারিওতে নয়

Fully automated low-risk FAQ only flows।
