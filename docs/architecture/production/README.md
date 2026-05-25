# Production architecture

Guides for turning the **pattern examples** in this repo into **deployable agent systems**. These docs are diagram- and decision-focused — they do not ship Kubernetes manifests or a hosted API (yet).

**Prerequisites:** Run at least [01 ReAct](../../patterns/01-react/) and read [single-agent vs multi-agent](../single-vs-multi-agent.md).

## Guides

| Doc | What you learn |
|-----|----------------|
| [Reference architecture](reference-architecture.md) | Sync chat, multi-agent, and event-driven topologies mapped to patterns |
| [Production concerns](production-concerns.md) | Timeouts, retries, idempotent tools, HITL approval flows, audit logs |
| [RAG at scale](rag-at-scale.md) | Indexing, chunking, refresh, when RAG vs tools — extends [11-rag](../../patterns/11-rag/) |
| [Observability & evals](observability-and-evals.md) | Traces, tool-call logging, offline evaluation — extends [08-evaluator-optimizer](../../patterns/08-evaluator-optimizer/) |
| [Scenario deployments](scenario-deployments.md) | IT helpdesk, e-commerce, and ML pipeline as production systems |

## How this relates to pattern folders

```
Learn pattern (patterns/XX/)  →  Run example (example/main.py)  →  Production guide (this folder)
```

| Repo layer | Teaches |
|------------|---------|
| `patterns/` | **What** each design pattern is |
| `example/` | **How** to implement it in LangGraph |
| `docs/architecture/production/` | **How to ship** it with real infra boundaries |

## Intentionally out of scope (for now)

- LangGraph Platform / managed durable execution
- Full CI/CD, Terraform, or cloud-specific runbooks
- Generic distributed-systems tutorials unrelated to agents

Link to official docs or a separate infra repo when you need those.

## Suggested reading order

1. [Reference architecture](reference-architecture.md)
2. [Production concerns](production-concerns.md)
3. Pick one: [RAG at scale](rag-at-scale.md) or [Observability & evals](observability-and-evals.md)
4. [Scenario deployments](scenario-deployments.md) for your domain
