> **English** | [বাংলা](use-case.bn.md)

# Use Case: Routing — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — one chat entry point handles VPN, password, and email requests with different playbooks.

## Why routing fits

A single generalist prompt dilutes quality and may invoke wrong tools. A router classifies intent first, then dispatches to a VPN, identity, or email handler—each with focused prompts and tool sets aligned to that domain.

## Example flow

1. User: “I forgot my password and MFA app is on a new phone.”
2. Router classifies intent → `identity/password`.
3. Identity handler runs with password-reset and MFA tools only.
4. Handler returns SSO reset steps and MFA re-enrollment link.
5. Router logs route label for analytics (`identity` vs `vpn` vs `email`).
6. User gets a domain-specific answer without unrelated VPN guidance.

## Out of scope

Mid-conversation tier escalation (see Handoff) and orchestrated multi-worker teams.
