# Use Case: Prompt Chaining — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — inbound chat messages are normalized into consistent, policy-compliant replies.

## Why prompt chaining fits

Tier-1 responses follow a repeatable pipeline: extract the issue, classify category, draft guidance, format for the portal. Fixed LLM stages are easy to test, log, and tune independently—no branching until you need routing.

## Example flow

1. Raw user message: “VPN drops every few minutes, already rebooted.”
2. **Extract** stage → `{ issue: "VPN disconnects", tried: ["reboot"] }`.
3. **Classify** stage → category `connectivity/vpn`.
4. **Draft** stage → troubleshooting bullets from policy tone.
5. **Format** stage → short reply with numbered steps and escalation note.
6. User receives formatted answer; each stage output is logged for QA.

## Out of scope

Tool calls mid-pipeline and conditional specialist routing.
