> [English](single-vs-multi-agent.md) | **বাংলা**

# Single-Agent বনাম Multi-Agent

এজেন্টিক সিস্টেম প্রায়ই **কতগুলো স্বায়ত্তশাসী এজেন্ট** লক্ষ্যে পৌঁছাতে সমন্বয় করে — তার দ্বারা বর্ণিত হয়। এই রিপোর বেশিরভাগ প্যাটার্ন এক বা উভয় মডেলে প্রযোজ্য।

## Single-agent

এক LLM-চালিত এজেন্ট শুরু থেকে শেষ কাজের দায়িত্বে। অনেক টুল, prompt ধাপ, বা ReAct লুপ থাকতে পারে — কিন্তু **এক সিদ্ধান্ত-গ্রহণকারী**, এক logical identity।

**বৈশিষ্ট্য**

- একটি context thread
- ডিবাগ, ডিপ্লয়, observe সহজ
- কম coordination overhead ও খরচ
- সব ক্ষমতা এক prompt + টুল সেটে ধরতে হয়

**Single-agent-এ সাধারণ প্যাটার্ন**

| প্যাটার্ন | ভূমিকা |
|----------|--------|
| [ReAct](../../patterns/01-react/) | think → act → observe |
| [Tool Use](../../patterns/02-tool-use/) | বিশ্বে প্রভাব |
| [Planning](../../patterns/03-planning/) | নিজের কাজ ভাঙা |
| [Prompt Chaining](../../patterns/04-prompt-chaining/) | ক্রমিক ধাপ, এক identity |
| [Evaluator–Optimizer](../../patterns/08-evaluator-optimizer/) | খসড়া ও সংশোধন |
| [Memory](../../patterns/10-memory/) | session state |
| [RAG](../../patterns/11-rag/) | grounding |
| [Guardrails](../../patterns/12-guardrails/) | নীতি |
| [HITL](../../patterns/09-human-in-the-loop/) | ঝুঁকিপূর্ণ ধাপে pause |

**উপযুক্ত যখন:** সংকীর্ণ ডোমেই, latency/খরচ গুরুত্বপূর্ণ, শক্তিশালী generalist + টুল যথেষ্ট।

---

## Multi-agent

**দুই বা ততোধিক এজেন্ট** — ভিন্ন ভূমিকা, prompt, টুল — সহযোগিতা করে। coordinator কাজ বরাদ্দ; parallel চলতে পারে বা **handoff** mid-task।

**বৈশিষ্ট্য**

- concern separation
- জটিলতা: state, handoff, conflict
- broad/multi-domain কাজে часто ভাল
- *কোন* এজেন্ট *কী* করল — audit সহজ

**Multi-agent-এ সাধারণ প্যাটার্ন**

| প্যাটার্ন | ভূমিকা |
|----------|--------|
| [Orchestrator–Workers](../../patterns/07-orchestrator-workers/) | supervisor → specialists |
| [Handoff](../../patterns/13-handoff/) | peer transfer |
| [Routing](../../patterns/05-routing/) | specialist-এ পাঠানো |
| [Parallelization](../../patterns/06-parallelization/) | একসাথে অনেক worker |
| [Map–Reduce](../../patterns/14-map-reduce/) | map + merge |

**উপযুক্ত যখন:** expertise area ভিন্ন, parallel speed দরকার, স্পষ্ট role boundary।

---

## উভয়ে কাজ করে

[Guardrails](../../patterns/12-guardrails/), [HITL](../../patterns/09-human-in-the-loop/), [Memory](../../patterns/10-memory/), [RAG](../../patterns/11-rag/), [Event-Driven](../../patterns/15-event-driven/) — single বা multi উভয় setup-এ।

---

## কীভাবে বেছে নিবেন

| প্রশ্ন | Single | Multi |
|--------|--------|-------|
| ডোমেইন | এক স্পষ্ট | একাধিক specialty |
| Audit | এক owner যথেষ্ট | role অনুযায়ী “কে করল?” |
| Latency | tight | coordination সহ্য |
| Implementation | দ্রুত ship | state, handoff wiring |

**নিয়ম:** **single-agent** দিয়ে ReAct + tools + guardrails। **multi-agent** যখন prompt/tool overload, true parallelism, বা explicit delegation দরকার।

---

## উদাহরণ কোথায়

| আর্কিটেকচার | শুরু |
|------------|------|
| Single-agent | [patterns/01-react](../../patterns/01-react/) |
| Multi-agent | [patterns/07-orchestrator-workers](../../patterns/07-orchestrator-workers/) + [patterns/13-handoff](../../patterns/13-handoff/) |

প্রতিটি `use-case.bn.md`-তে single, multi, বা hybrid উল্লেখ করুন।
