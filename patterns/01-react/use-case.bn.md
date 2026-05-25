> [English](use-case.md) | **বাংলা**

# Use Case: ReAct — Corp IT Helpdesk

শেয়ার্ড সিনারিও: [Corp IT Helpdesk](../../docs/bn/use-cases/it-helpdesk.md) — VPN, password reset, Outlook issues।

## কেন ReAct মানায়

Helpdesk triage এক shot নয় — symptom নিয়ে চিন্তা, FAQ/status টুল, observe, escalate সিদ্ধান্ত। ReAct think→act→observe fixed pipeline ছাড়াই iterative troubleshoot-এ মানায়।

## উদাহরণ ফ্লো

1. User: "VPN disconnect; restart করেছি।"
2. Agent: FAQ-এ VPN steps খুঁজব।
3. `search_faq` → reset steps observe।
4. Gateway status check।
5. outage/blocked হলে `create_ticket`।
6. Actionable steps + ticket ID।

## এই সিনারিওতে নয়

Bulk incident, multi-agent routing, human approval (অন্য প্যাটার্ন)।
