# Use Case: Parallelization — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — employees expect fast answers even when several checks are independent.

## Why parallelization fits

VPN troubleshooting often needs FAQ snippets, VPN gateway status, and email service health at once. Those lookups do not depend on each other—running them concurrently cuts latency before merging into one coherent reply.

## Example flow

1. User: “VPN drops and Outlook sync is slow.”
2. Graph fans out three branches in parallel:
   - FAQ search for VPN disconnects
   - `check_vpn_status`
   - `check_email_status`
3. Merge node waits for all branches (~single round-trip time).
4. Synthesizer LLM combines findings: degraded VPN region + email OK.
5. Final reply: VPN steps plus note that Outlook slowness is likely VPN-related.
6. User sees one merged answer faster than three sequential tool rounds.

## Out of scope

Chunked batch processing over hundreds of incidents (see Map–Reduce).
