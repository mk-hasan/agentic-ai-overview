> [English](../patterns/README.md) | **বাংলা**

# এজেন্টিক AI ডিজাইন প্যাটার্ন

স্বায়ত্তশাসী ও আধা-স্বায়ত্তশাসী AI এজেন্ট তৈরির সাধারণ প্যাটার্নের ক্যাটালগ। প্রতিটি প্যাটার্ন [`patterns/`](../../patterns/)-এর নিজস্ব ফোল্ডারে — বাস্তব use case ও runnable উদাহরণের জন্য জায়গা।

**আর্কিটেকচার:** [Single-agent বনাম multi-agent](../architecture/single-vs-multi-agent.md)

## প্যাটার্ন ইনডেক্স

| # | প্যাটার্ন | বিভাগ | ফোল্ডার |
|---|----------|-------|---------|
| 01 | [ReAct](../../patterns/01-react/) | Core loop | `patterns/01-react/` |
| 02 | [Tool Use](../../patterns/02-tool-use/) | Core loop | `patterns/02-tool-use/` |
| 03 | [Planning](../../patterns/03-planning/) | Core loop | `patterns/03-planning/` |
| 04 | [Prompt Chaining](../../patterns/04-prompt-chaining/) | Workflow | `patterns/04-prompt-chaining/` |
| 05 | [Routing](../../patterns/05-routing/) | Workflow | `patterns/05-routing/` |
| 06 | [Parallelization](../../patterns/06-parallelization/) | Workflow | `patterns/06-parallelization/` |
| 07 | [Orchestrator–Workers](../../patterns/07-orchestrator-workers/) | Workflow | `patterns/07-orchestrator-workers/` |
| 08 | [Evaluator–Optimizer](../../patterns/08-evaluator-optimizer/) | Workflow | `patterns/08-evaluator-optimizer/` |
| 09 | [Human-in-the-Loop](../../patterns/09-human-in-the-loop/) | Control | `patterns/09-human-in-the-loop/` |
| 10 | [Memory](../../patterns/10-memory/) | Control | `patterns/10-memory/` |
| 11 | [RAG](../../patterns/11-rag/) | Control | `patterns/11-rag/` |
| 12 | [Guardrails](../../patterns/12-guardrails/) | Control | `patterns/12-guardrails/` |
| 13 | [Handoff](../../patterns/13-handoff/) | Advanced | `patterns/13-handoff/` |
| 14 | [Map–Reduce](../../patterns/14-map-reduce/) | Advanced | `patterns/14-map-reduce/` |
| 15 | [Event-Driven](../../patterns/15-event-driven/) | Advanced | `patterns/15-event-driven/` |

## বিভাগ

- **Core loop** — এক এজেন্ট কীভাবে চিন্তা, সিদ্ধান্ত, কাজ করে।
- **Workflow** — ধাপ বা এজেন্ট পাইপলাইনে কীভাবে মিলিত হয়।
- **Control** — মানুষের তত্ত্বাবধান, স্মৃতি, রিট্রিভাল, নিরাপত্তা।
- **Advanced** — delegation, স্কেল, reactive আর্কিটেকচার।

## নতুন উদাহরণ যোগ করা

1. [`templates/pattern-example/`](../../templates/pattern-example/) কপি করুন।
2. `use-case.bn.md`-তে সমস্যা, অভিনেতা, সফলতার মানদণ্ড লিখুন।
3. `example/` বাস্তবায়ন ও README.bn.md-তে রান ধাপ।
4. প্যাটার্ন `README.bn.md` থেকে লিংক করুন।

**শুরু:** [getting-started.md](../getting-started.md) — প্রথম **01 ReAct**, তারপর **02 Tool Use**।

**শেয়ার্ড সিনারিও:** [Corp IT Helpdesk](../use-cases/it-helpdesk.md) — ১৫টি উদাহরণ। [রান কমান্ড](../use-cases/run-all-examples.md)।
