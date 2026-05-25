> [English](use-case.md) | **বাংলা**

# Use Case: Planning — Corp IT Helpdesk

শেয়ার্ড সিনারিও: [Corp IT Helpdesk](../../docs/bn/use-cases/it-helpdesk.md) — VPN, password reset, Outlook issues।

## কেন Planning মানায়

VPN + Outlook একসাথে fail — dependency সহ ordered troubleshoot plan দরকার, random tool call নয়।

## উদাহরণ ফ্লো

1. User: VPN + Outlook issue।
2. Plan: network → auth → mail client।
3. Step 1: VPN FAQ + status।
4. Step 2: password/MFA verify।
5. Step 3: Outlook cache steps।
6. Plan complete → unified reply।

## এই সিনারিওতে নয়

Single FAQ lookup, static chain only।
