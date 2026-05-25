# Use Case: Map–Reduce — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — leadership needs summaries across many VPN-related incidents, not one chat reply.

## Why map–reduce fits

Weekly incident JSON logs are too large for one prompt. Map workers summarize each incident independently; a reduce step merges partial summaries into an executive report—themes, affected regions, mean time to resolve—without hitting context limits.

## Example flow

1. Input: batch of incident records from `incidents.json` (VPN outages, auth failures).
2. **Map:** each incident → one-line summary (category, duration, resolution).
3. Partial summaries collected in parallel or sequence.
4. **Reduce:** synthesizer LLM produces executive report—top themes, repeat offenders, recommendations.
5. IT manager receives aggregate view, not 50 individual narratives.
6. Report stored for staff meeting; drill-down uses original incident IDs.

## Out of scope

Real-time single-user chat triage and interactive troubleshooting loops.
