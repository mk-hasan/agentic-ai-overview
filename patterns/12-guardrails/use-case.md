# Use Case: Guardrails — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — the bot faces untrusted employee input and must refuse unsafe or non-compliant requests.

## Why guardrails fits

Users may paste SSNs, credentials, or ask the bot to disable security controls. Input filters block PII and policy violations before the agent runs; output checks ensure replies do not leak secrets or bypass approval rules.

## Example flow

1. Normal request: VPN disconnect question → passes input guard → agent answers from FAQ.
2. User adds: “My SSN is 123-45-6789 for verification.”
3. Input guard detects PII → blocks before LLM call.
4. Agent returns safe refusal: ask user to remove sensitive data; offer ticket path.
5. Output guard (on allowed runs) redacts any accidental credential echoes.
6. Incident logged for security review without storing raw PII in prompts.

## Out of scope

Human manager approval for ticket creation (see Human-in-the-Loop).
