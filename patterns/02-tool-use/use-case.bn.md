> [English](use-case.md) | **বাংলা**

# Use Case: Tool Use — Corp IT Helpdesk

শেয়ার্ড সিনারিও: [Corp IT Helpdesk](../../docs/bn/use-cases/it-helpdesk.md) — VPN, password reset, Outlook issues।

## কেন Tool Use মানায়

Helpdesk live ticket system, VPN status, employee directory — structured tool call ছাড়া reliable integration কঠিন।

## উদাহরণ ফ্লো

1. User password reset চায়।
2. `lookup_employee` → account status।
3. `search_faq` → reset policy।
4. `check_vpn_status` → gateway OK।
5. Policy-compliant steps + optional ticket tool।

## এই সিনারিওতে নয়

শুধু static FAQ text, টুল schema ছাড়া।
