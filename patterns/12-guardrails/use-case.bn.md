> [English](use-case.md) | **বাংলা**

# Use Case: Guardrails — Corp IT Helpdesk

শেয়ার্ড সিনারিও: [Corp IT Helpdesk](../../docs/bn/use-cases/it-helpdesk.md) — VPN, password reset, Outlook issues।

## কেন Guardrails মানায়

SSN/phone in ticket — input/output PII block before agent or side effects।

## উদাহরণ ফ্লো

1. User message with sensitive patterns।
2. Guardrail pre-check blocks/redacts।
3. Agent runs on safe content only।
4. Post-check before ticket/email tools।
5. Refusal or redacted safe reply।

## এই সিনারিওতে নয়

Trusted internal-only with zero policy (still risky)।
