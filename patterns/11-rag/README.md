# Retrieval-Augmented Generation (RAG)

## What it is

Before generating, the agent **retrieves relevant documents** from a knowledge base and grounds the answer in that context—reducing hallucination on domain facts.

## When to use it

- Internal docs, policies, product catalogs, support KB.
- Facts change often and cannot live only in model weights.
- Citations and traceability matter.

## When not to use it

- All needed knowledge fits reliably in the prompt.
- Retrieval quality is poor without major indexing investment.

## Related patterns

- [Memory](../10-memory/) — RAG as long-term semantic memory
- [Tool Use](../02-tool-use/) — search as a tool vs. automatic RAG step
- [Parallelization](../06-parallelization/) — retrieve from many indexes in parallel

## Example

See [`example/`](example/) — **LangGraph RAG demo** (IT helpdesk: retrieve from markdown KB, then answer with tools).

Run from repo root: `python patterns/11-rag/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** HR policy bot, technical documentation Q&A, legal clause lookup.
