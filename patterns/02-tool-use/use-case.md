> **English** | [বাংলা](use-case.bn.md)

# Use Case: Tool Use — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — the assistant must pull live FAQ entries, ticket history, and service status instead of guessing.

## Why tool use fits

Helpdesk answers depend on systems of record: knowledge base, ticketing API, and status dashboards. Function calling gives structured, auditable access—each fact comes from a named tool with a schema, not free-form invention.

## Example flow

1. User asks about VPN disconnects.
2. Model selects `search_faq` with query `"vpn disconnect"`.
3. Runtime returns matching KB snippet.
4. Model selects `check_vpn_status` → observes “degraded in US-East.”
5. Model selects `create_ticket` with category `vpn` and summary.
6. Final reply cites tool results and next steps for the employee.

## Out of scope

Dynamic routing to specialist agents and guardrail policy checks (covered in patterns 05 and 12).
