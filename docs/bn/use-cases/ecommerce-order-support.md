> [English](../use-cases/ecommerce-order-support.md) | **বাংলা**

# Use Case: E-commerce Order Support

সব প্যাটার্ন উদাহরণের দ্বিতীয় শেয়ার্ড সিনারিও। IT helpdesk-এর মতো LangGraph প্যাটার্ন, ভিন্ন ডোমেই।

তুলনা: [IT Helpdesk](it-helpdesk.md)।

## সমস্যা

অনলাইন ক্রেতারা অর্ডার status, shipping, return, refund নিয়ে সাপোর্টে যোগাযোগ করে। Tier-1 lookup ও নীতি; Tier-2 exception ও refund।

## অভিনেতা

| অভিনেতা | ভূমিকা |
|---------|--------|
| Customer (Jordan Lee) | অর্ডার #48291 — delivery ও address |
| Tier-1 bot | নীতি, order lookup, shipping |
| Tier-2 bot | refund, জটিল delivery |
| Manager (human) | threshold-এর উপর refund approve |

## বেসলাইন অনুরোধ

*"অর্ডার #48291 কোথায়? গত সপ্তাহে অর্ডার; শুক্রবারের আগে delivery চাই।"*

## প্যাটার্ন অনুযায়ী

| প্যাটার্ন | E-commerce সম্প্রসারণ |
|----------|---------------------|
| 03 Planning | lookup → shipping → advise/escalate |
| 05 Routing | orders / shipping / returns / billing |
| 06 Parallel | policies + order + carrier |
| 09 HITL | `request_refund` approve |
| 10 Memory | shipping address change follow-up |
| 11 RAG | returns/shipping policy markdown |
| 13 Handoff | Tier-1 → Tier-2 refund |
| 14 Map–reduce | CS ticket batch summary |
| 15 Event-driven | “order delayed” email |

## চালান

```bash
python patterns/01-react/example/main.py --scenario ecommerce --provider openai
python patterns/01-react/example/ecommerce/main.py --provider deepseek
```

## শেয়ার্ড কোড

`shared/examples/ecommerce/` — tools, `data/kb/`।
