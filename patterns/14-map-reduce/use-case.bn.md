> [English](use-case.md) | **বাংলা**

# Use Case: Map–Reduce — Corp IT Helpdesk

শেয়ার্ড সিনারিও: [Corp IT Helpdesk](../../docs/bn/use-cases/it-helpdesk.md) — VPN, password reset, Outlook issues।

## কেন Map–Reduce মানায়

অনেক incident log — parallel summarize per chunk, reduce executive report।

## উদাহরণ ফ্লো

1. Batch incident JSON input।
2. Map: summarize each incident/chunk।
3. Reduce: themes, counts, priorities।
4. Executive summary for manager।

## এই সিনারিওতে নয়

Single short message needing full global context in one pass।
