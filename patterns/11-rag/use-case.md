# Use Case: RAG — Corp IT Helpdesk

Shared scenario: [Corp IT Helpdesk](../../docs/use-cases/it-helpdesk.md) — answers must come from the internal KB (VPN, password reset, Outlook guides), not model memory.

## Why RAG fits

Policy and runbooks change frequently. Retrieving relevant markdown chunks before generation grounds replies in current docs—reducing hallucinated steps—and enables citations to `vpn-disconnects.md` or `password-reset.md`.

## Example flow

1. User: “VPN keeps disconnecting; I restarted once.”
2. Retriever embeds query → top chunks from KB markdown files.
3. Agent node receives user message plus retrieved context in the prompt.
4. Agent may still call tools (status, tickets) but bases steps on KB text.
5. Reply includes accurate corp-specific steps (split tunnel, MFA, client version).
6. Support can trace which KB sections informed the answer.

## Out of scope

Replacing the KB with a static FAQ dict only (see ReAct starter tools).
