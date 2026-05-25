> **English** | [বাংলা](use-case.bn.md)

# Use Case: Planning — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — some requests need ordered steps (diagnose → verify → escalate) before the agent acts.

## Why planning fits

Complex tickets waste tokens when the model retries tools randomly. Upfront decomposition produces a checklist—FAQ lookup, status check, user confirmation, ticket creation—so each step runs in dependency order with room to replan if a step fails.

## Example flow

1. User reports VPN plus Outlook failures after a laptop restart.
2. Planner LLM outputs: (1) search FAQ for VPN, (2) check VPN status, (3) search FAQ for Outlook, (4) open ticket if unresolved.
3. Executor runs step 1 → FAQ steps returned.
4. Executor runs steps 2–3 → status OK, Outlook cache steps found.
5. Planner revises: skip ticket; deliver combined instructions.
6. Final answer: ordered troubleshooting for both apps.

## Out of scope

Parallel status fan-out and specialist worker delegation.
