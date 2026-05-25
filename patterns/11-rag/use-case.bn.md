> [English](use-case.md) | **বাংলা**

# Use Case: RAG — Corp IT Helpdesk

শেয়ার্ড সিনারিও: [Corp IT Helpdesk](../../docs/bn/use-cases/it-helpdesk.md) — VPN, password reset, Outlook issues।

## কেন RAG মানায়

Policy/playbook markdown KB — hard-coded dict-এর বদলে retrieve + cite grounded answers।

## উদাহরণ ফ্লো

1. User VPN policy question।
2. Retrieve relevant KB chunks।
3. Agent answers with retrieved context।
4. Optional tools for status/ticket।
5. Grounded reply with KB reference।

## এই সিনারিওতে নয়

All knowledge fits in static prompt reliably।
