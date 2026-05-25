> **English** | [বাংলা](../bn/use-cases/ecommerce-order-support.md)

# Use Case: E-commerce Order Support

Second shared scenario for all pattern examples. Same LangGraph patterns as IT helpdesk, different domain.

Master reference: compare with [IT Helpdesk](it-helpdesk.md).

## Problem

Online shoppers contact support about order status, shipping changes, returns, and refunds. Tier-1 resolves lookups and policy questions; Tier-2 handles exceptions and refunds.

## Actors

| Actor | Role |
|-------|------|
| Customer (Jordan Lee) | Order #48291 — delivery and address questions |
| Tier-1 bot | Policies, order lookup, shipping status |
| Tier-2 bot | Refunds, complex delivery failures |
| Manager (human) | Approves refunds over policy thresholds |

## Baseline request

*"Where is my order #48291? I ordered last week and need it delivered by Friday."*

## Extended flows (by pattern)

| Pattern | E-commerce extension |
|---------|---------------------|
| 03 Planning | Plan: lookup order → check shipping → advise or escalate |
| 05 Routing | Route to orders / shipping / returns / billing |
| 06 Parallel | Policies + order details + carrier status in parallel |
| 09 HITL | Human approves `request_refund` before execution |
| 10 Memory | Follow-up: change shipping address before delivery |
| 11 RAG | Ground answers in returns/shipping policy markdown |
| 13 Handoff | Tier-1 → Tier-2 for refund exceptions |
| 14 Map–reduce | Summarize CS ticket batch (`ecommerce/data/incidents.json`) |
| 15 Event-driven | Inbound “order delayed” email event |

## Run

```bash
python patterns/01-react/example/main.py --scenario ecommerce --provider openai
python patterns/01-react/example/ecommerce/main.py --provider deepseek
```

## Shared code

`shared/examples/ecommerce/` — tools (`get_order`, `search_policies`, `create_return`, …), KB under `data/kb/`.
