# Use Case: Evaluator–Optimizer — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — replies must be clear, actionable, and aligned with support policy before reaching employees.

## Why evaluator–optimizer fits

First-draft answers can be vague or miss escalation rules. A separate evaluator scores drafts on completeness, tone, and policy compliance; the optimizer revises until the score passes—raising quality without manual rewrite on every ticket.

## Example flow

1. User asks about recurring VPN disconnects.
2. **Generator** drafts: generic “restart your router” advice.
3. **Evaluator** scores low—missing corp VPN client steps and ticket policy.
4. **Optimizer** revises with FAQ steps, MFA check, and when to open a ticket.
5. Evaluator re-scores → passes threshold after round 2.
6. Employee receives the polished reply; score and rounds logged for QA.

## Out of scope

Hard PII blocks and interactive human approval (patterns 09 and 12).
