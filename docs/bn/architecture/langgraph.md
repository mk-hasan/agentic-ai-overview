> [English](langgraph.md) | **বাংলা**

# LangGraph

এই রিপোর সব runnable উদাহরণ **[LangGraph](https://langchain-ai.github.io/langgraph/)** ব্যবহার করে।

## কেন LangGraph

- **গ্রাফ-ভিত্তিক ফ্লো** সরাসরি ডিজাইন প্যাটার্নের সাথে মিলে (ReAct, routing, multi-agent)।
- **শেয়ার্ড state** — স্মৃতি ও পরিকল্পনা।
- **Checkpoints & interrupts** — HITL ও persistence।
- **Prebuilt components** — `ToolNode`, `tools_condition` ইত্যাদি।

LangChain Core বার্তা ও টুল দেয়; পুরো LangChain স্ট্যাক দরকার নেই।

## স্ট্যান্ডার্ড example কাঠামো

```
patterns/XX-name/example/
├── main.py
├── graph.py
├── tools.py
└── README.bn.md
```

শেয়ার্ড সেটআপ [`shared/`](../../shared/)-এ:

| মডিউল | উদ্দেশ্য |
|-------|---------|
| `shared/utils/env.py` | রুট `.env` লোড |
| `shared/utils/llm.py` | OpenAI / DeepSeek মডেল |
| `shared/examples/cli.py` | `--scenario`, `--provider` ইত্যাদি |

## ইনস্টল

```bash
pip install -e .
cp .env.example .env
```

## LLM প্রোভাইডার

| প্রোভাইডার | Env |
|------------|-----|
| OpenAI | `OPENAI_API_KEY`, `OPENAI_MODEL` |
| DeepSeek | `DEEPSEEK_API_KEY`, `DEEPSEEK_MODEL` |

```bash
python patterns/01-react/example/main.py --provider deepseek
```

## সিনারিও

| সিনারিও | বর্ণনা |
|---------|--------|
| `helpdesk` (ডিফল্ট) | IT সাপোর্ট |
| `ecommerce` | অর্ডার #48291 |
| `demand-forecast` | SKU চাহিদা পূর্বাভাস MLDLC |

```bash
python patterns/01-react/example/main.py --scenario ecommerce
```

## প্যাটার্ন → LangGraph ম্যাপিং

| প্যাটার্ন | LangGraph পদ্ধতি |
|----------|------------------|
| 01 ReAct | Agent + `ToolNode` + `tools_condition` |
| 02 Tool Use | `@tool` + `ToolNode` |
| 03 Planning | Plan node → sequential nodes |
| 04 Prompt Chaining | রৈখিক node chain |
| 05 Routing | `add_conditional_edges` |
| 06 Parallelization | Parallel branches / `Send` |
| 07 Orchestrator–Workers | Supervisor + worker subgraphs |
| 08 Evaluator–Optimizer | Generate ↔ evaluate loop |
| 09 HITL | `interrupt()` + SQLite + time travel |
| 10 Memory | SQLite + `thread_id` |
| 11 RAG | Retrieve node → agent |
| 12 Guardrails | Pre/post nodes |
| 13 Handoff | Command routing |
| 14 Map–Reduce | Map `Send` + reduce |
| 15 Event-Driven | Nested subgraph + event stream |

## এই রিপোতে LangGraph ক্ষমতা

| ক্ষমতা | প্যাটার্ন | কীভাবে |
|--------|----------|--------|
| **Persistence** | 09, 10 | SQLite — `data/checkpoints/langgraph.db` |
| **Interrupts** | 09 | side-effect টুলের আগে pause |
| **Time travel** | 09 | `--time-travel` |
| **Subgraphs** | 07, 15 | worker / event handler subgraphs |
| **Chat streaming** | 01, 02 | `stream_mode="messages"` |
| **Event streaming** | 07, 15 | `stream_mode="updates"` |

```bash
python patterns/09-human-in-the-loop/example/main.py --auto-approve --time-travel
python patterns/07-orchestrator-workers/example/main.py --scenario demand-forecast --no-mlflow
```

এখনো দেখানো হয়নি: LangGraph Platform durable execution, fault tolerance, Store API।

## স্টার্টার

[`patterns/01-react/example/`](../../patterns/01-react/example/) — IT হেল্পডেস্ক ReAct।
