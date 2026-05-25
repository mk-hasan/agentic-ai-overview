> **English** | [বাংলা](use-case.bn.md)

# Use Case: Orchestrator–Workers — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — complex tickets span VPN, identity, and email systems with distinct expertise.

## Why orchestrator–workers fits

No single agent should own every subsystem. A supervisor decomposes the case and delegates to specialist workers (VPN, password/MFA, Outlook)—each with tailored prompts and tools—then synthesizes a unified response for the employee.

## Example flow

1. User: “VPN fails after password reset; Outlook won’t sync.”
2. Orchestrator assigns VPN worker → returns client reset steps.
3. Orchestrator assigns identity worker → confirms SSO token refresh.
4. Orchestrator assigns email worker → Outlook cache clear steps.
5. Orchestrator merges worker outputs, removes duplicates, sets priority.
6. User receives one coordinated plan referencing all three areas.

## Out of scope

Simple single-domain FAQ lookups and static prompt pipelines.
