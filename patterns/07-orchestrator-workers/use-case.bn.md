> [English](use-case.md) | **বাংলা**

# Use Case: Orchestrator–Workers — Corp IT Helpdesk

শেয়ার্ড সিনারিও: [Corp IT Helpdesk](../../docs/bn/use-cases/it-helpdesk.md) — VPN, password reset, Outlook issues।

## কেন Orchestrator–Workers মানায়

VPN + identity + email — এক agent সব subsystem own করবে না; supervisor delegate করে specialist workers-এ।

## উদাহরণ ফ্লো

1. User: VPN fail after password reset; Outlook sync fail।
2. VPN worker → client reset steps।
3. Identity worker → SSO token refresh।
4. Email worker → Outlook cache clear।
5. Orchestrator merge, dedupe, priority।
6. One coordinated plan।

## এই সিনারিওতে নয়

Simple single-domain FAQ।
