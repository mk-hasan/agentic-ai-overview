> **English** | [বাংলা](use-case.bn.md)

# Use Case: ReAct — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — employees report VPN drops, password resets, and Outlook issues via chat.

## Why ReAct fits

Helpdesk triage is rarely one shot. The agent must reason about symptoms, call FAQ or status tools, observe results, and decide whether to escalate. ReAct’s think → act → observe loop matches that iterative troubleshooting without a fixed pipeline.

## Example flow

1. User: “VPN keeps disconnecting; I restarted once.”
2. Agent thinks: check FAQ for VPN disconnect steps.
3. Agent calls `search_faq` → observes reset-and-reconnect steps.
4. Agent thinks: steps may not suffice; checks VPN gateway status.
5. Agent calls `create_ticket` if status shows an outage or user still blocked.
6. Final answer: actionable steps plus ticket ID if opened.

## Out of scope

Bulk incident reporting, multi-agent routing, and human approval gates (see other patterns).
