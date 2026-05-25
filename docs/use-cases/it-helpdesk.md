> **English** | [বাংলা](../bn/use-cases/it-helpdesk.md)

# Use Case: Corp IT Helpdesk

Default scenario (`--scenario helpdesk`) for all pattern examples. See also [E-commerce Order Support](ecommerce-order-support.md).

## Problem

Employees contact IT about VPN drops, password lockouts, and email sync failures. Tier-1 must resolve common issues quickly, escalate complex cases, and avoid unsafe actions (PII leaks, policy bypass requests).

## Actors

| Actor | Role |
|-------|------|
| Employee (Alex Jordan) | Reports issues via chat or email |
| Tier-1 agent | FAQ, status checks, initial troubleshooting |
| Tier-2 specialist | Deep VPN/network investigation |
| Manager (human) | Approves ticket creation when required |
| Event system | Delivers inbound support emails |

## Baseline scenario (patterns 01–02)

**Request:** *"My VPN keeps disconnecting every few minutes. I already restarted my laptop."*

**Expected flow:** Search FAQ → check VPN status → suggest steps → open ticket if unresolved.

## Extended scenario (patterns 03–15)

| Phase | Pattern(s) | Extension |
|-------|------------|-----------|
| Planning | 03 | Agent decomposes troubleshooting into steps |
| Pipeline | 04 | Extract → classify → draft → format reply |
| Routing | 05 | Route vpn / password / email intents |
| Parallel | 06 | FAQ + VPN status + email status in parallel |
| Multi-agent | 07 | Orchestrator assigns VPN/password/email workers |
| Quality | 08 | Draft reply scored and revised |
| Approval | 09 | Human approves ticket before creation |
| Memory | 10 | Follow-up: *"VPN worked briefly, now Outlook fails too"* |
| Knowledge | 11 | Answers grounded in markdown KB (not hard-coded dict) |
| Safety | 12 | Block requests containing SSN/phone patterns |
| Escalation | 13 | Tier-1 hands off to Tier-2 (collect VPN logs) |
| Batch | 14 | Summarize multiple incident logs into one report |
| Async | 15 | Process inbound support email webhook event |

## Success criteria

- Actionable troubleshooting steps from FAQ/KB
- Tickets only when needed (and approved when policy requires)
- No sensitive data in tickets or replies
- Complex VPN cases escalated with log collection

## Shared code

| Location | Contents |
|----------|----------|
| `shared/examples/helpdesk/tools.py` | FAQ search, tickets, status, employee lookup |
| `shared/examples/helpdesk/data/kb/` | Markdown knowledge base (RAG) |
| `shared/examples/helpdesk/data/incidents.json` | Batch logs (map–reduce) |
| `shared/examples/helpdesk/data/sample_event.json` | Email event (event-driven) |

## Run any example

```bash
python patterns/XX-pattern/example/main.py --provider openai
python patterns/XX-pattern/example/main.py --provider deepseek
```

Replace `XX-pattern` with e.g. `03-planning`, `11-rag`.
