> [English](../use-cases/it-helpdesk.md) | **বাংলা**

# Use Case: Corp IT Helpdesk

সব প্যাটার্ন উদাহরণের ডিফল্ট সিনারিও (`--scenario helpdesk`)। [E-commerce](ecommerce-order-support.md)-ও দেখুন।

## সমস্যা

কর্মচারী VPN বিচ্ছিন্ন, পাসওয়ার্ড লক, ইমেইল sync সমস্যা নিয়ে IT-তে যোগাযোগ করে। Tier-1 দ্রুত সাধারণ সমস্যা সমাধান, জটিল কেস escalate, unsafe কাজ (PII leak, policy bypass) এড়াতে হয়।

## অভিনেতা

| অভিনেতা | ভূমিকা |
|---------|--------|
| Employee (Alex Jordan) | চ্যাট/ইমেইলে সমস্যা জানায় |
| Tier-1 agent | FAQ, status, প্রাথমিক troubleshoot |
| Tier-2 specialist | গভীর VPN/network |
| Manager (human) | প্রয়োজনে টিকেট অনুমোদন |
| Event system | ইনবাউন্ড support email |

## বেসলাইন (প্যাটার্ন 01–02)

**অনুরোধ:** *"VPN কয়েক মিনিট পর পর disconnect হয়; ল্যাপটপ restart করেছি।"*

**প্রত্যাশিত ফ্লো:** FAQ → VPN status → ধাপ → unresolved হলে টিকেট।

## Extended (প্যাটার্ন 03–15)

| পর্যায় | প্যাটার্ন | সম্প্রসারণ |
|---------|----------|-----------|
| Planning | 03 | troubleshoot ধাপে ভাঙা |
| Pipeline | 04 | extract → classify → draft → format |
| Routing | 05 | vpn / password / email |
| Parallel | 06 | FAQ + VPN + email status |
| Multi-agent | 07 | VPN/password/email workers |
| Quality | 08 | draft score ও revise |
| Approval | 09 | টিকেটের আগে human approve |
| Memory | 10 | follow-up: Outlook-ও fail |
| Knowledge | 11 | markdown KB grounding |
| Safety | 12 | SSN/phone block |
| Escalation | 13 | Tier-1 → Tier-2 |
| Batch | 14 | incident log summary |
| Async | 15 | inbound email event |

## সফলতার মানদণ্ড

- FAQ/KB থেকে actionable ধাপ
- প্রয়োজনে টিকেট (নীতি অনুযায়ী approved)
- sensitive data টিকেট/reply-তে নেই
- জটিল VPN escalate + log collection

## শেয়ার্ড কোড

| অবস্থান | বিষয়বস্তু |
|---------|-----------|
| `shared/examples/helpdesk/tools.py` | FAQ, ticket, status |
| `shared/examples/helpdesk/data/kb/` | Markdown KB (RAG) |
| `shared/examples/helpdesk/data/incidents.json` | map–reduce |
| `shared/examples/helpdesk/data/sample_event.json` | event-driven |

## যেকোনো উদাহরণ চালান

```bash
python patterns/XX-pattern/example/main.py --provider openai
python patterns/XX-pattern/example/main.py --provider deepseek
```

`XX-pattern` = `03-planning`, `11-rag` ইত্যাদি।
