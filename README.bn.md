> [English](README.md) | **বাংলা**

# Agentic AI Overview

**১৫টি এজেন্টিক AI ডিজাইন প্যাটার্ন**-এর হাতে-কলমে ক্যাটালগ — প্রতিটিতে **চালানো যায় এমন LangGraph উদাহরণ** এবং **তিনটি ভাগ করা বাস্তব-জগতের সিনারিও**। এজেন্ট কীভাবে তৈরি হয়, প্যাটার্ন কীভাবে একসাথে কাজ করে, এবং রেফারেন্স কোডকে প্রোডাকশনে কীভাবে মানিয়ে নিতে হয় — এগুলো শিখতে এই রিপো ব্যবহার করুন।

**নতুন?** [শুরু করা](docs/bn/getting-started.md) → [ReAct](patterns/01-react/) চালান → [single-agent বনাম multi-agent](docs/bn/architecture/single-vs-multi-agent.md) পড়ুন।

**English:** [README.md](README.md) · [English docs](docs/getting-started.md)

---

## এই রিপোতে কী আছে

| স্তর | যা পাবেন |
|------|----------|
| **প্যাটার্ন** (`patterns/01`–`15`) | প্রতি ডিজাইন প্যাটার্নে একটি ফোল্ডার: ধারণা README, use-case, কাজ করা `example/` |
| **সিনারিও** (`shared/examples/`) | তিনটি ডোমেই — mock টুল, প্রম্পট, ডেটা; `--scenario` দিয়ে বদলান |
| **শেয়ার্ড রানটাইম** (`shared/`) | LLM ক্লায়েন্ট, CLI, LangGraph হেল্পার, ঐচ্ছিক MCP সার্ভার, সিনারিও রেজিস্ট্রি |
| **ডক** (`docs/`) | আর্কিটেকচার, use-case গাইড, প্যাটার্ন ইনডেক্স, রান কমান্ড |
| **টেস্ট** (`tests/`) | টুল, CLI ফ্ল্যাগ, orchestrator লজিক, checkpointer-এর ইউনিট টেস্ট |

প্রতিটি প্যাটার্ন উদাহরণ **একই তিনটি সিনারিও**-তে চলে — IT সাপোর্ট, ই-কমার্স, বা ML পাইপলাইনে একটি প্যাটার্ন কীভাবে আচরণ করে তুলনা করতে পারবেন, ডোমেইন লজিক আবার লেখার দরকার নেই।

---

## তিনটি use case (সিনারিও)

সব উদাহরণ `--scenario helpdesk|ecommerce|demand-forecast` গ্রহণ করে:

| সিনারিও | ডোমেই | উদাহরণ প্রশ্ন | উল্লেখযোগ্য টুল |
|---------|-------|----------------|-----------------|
| **helpdesk** | কর্প IT সাপোর্ট | VPN বিচ্ছিন্ন, পাসওয়ার্ড রিসেট | FAQ অনুসন্ধান, টিকেট, VPN স্ট্যাটাস |
| **ecommerce** | অর্ডার সাপোর্ট | অর্ডার #48291 কোথায়? | অর্ডার lookup, শিপিং, রিটার্ন, রিফান্ড |
| **demand-forecast** | ML পাইপলাইন (MLDLC) | SKU চাহিদা পূর্বাভাস ট্রেন ও ডিপ্লয় | ডেটা লোড, মডেল ট্রেন, MLflow, রেজিস্টার |

ডক: [IT Helpdesk](docs/bn/use-cases/it-helpdesk.md) · [E-commerce](docs/bn/use-cases/ecommerce-order-support.md) · [Demand Forecast](docs/bn/use-cases/demand-forecast.md) · [সব উদাহরণ চালান](docs/bn/use-cases/run-all-examples.md)

কিছু প্যাটার্ন ফোল্ডারে shortcut আছে, যেমন `patterns/01-react/example/ecommerce/main.py`।

---

## দ্রুত শুরু

```bash
git clone <repo-url> && cd agentic-ai-overview
python -m venv .venv && source .venv/bin/activate
pip install -e .
cp .env.example .env
# .env-এ OPENAI_API_KEY এবং/অথবা DEEPSEEK_API_KEY সেট করুন
```

`pip install -e .` `shared` প্যাকেজ editable মোডে ইনস্টল করে — `PYTHONPATH` লাগে না।

প্রথম এজেন্ট চালান:

```bash
python patterns/01-react/example/main.py --scenario helpdesk --provider deepseek
python patterns/02-tool-use/example/main.py --scenario ecommerce --provider deepseek
```

ঐচ্ছিক extras:

```bash
pip install -e ".[dev]"   # pytest + SQLite checkpointer
pip install -e ".[ml]"    # MLflow (demand-forecast)
pip install -e ".[mcp]"   # MCP টুল সার্ভার (Python 3.10+)
```

---

## সাধারণ CLI ফ্ল্যাগ

প্রতিটি প্যাটার্ন উদাহরণ একই CLI শেয়ার করে (`shared/examples/cli.py`):

| ফ্ল্যাগ | উদ্দেশ্য |
|--------|---------|
| `--scenario helpdesk\|ecommerce\|demand-forecast` | use case বেছে নিন (ডিফল্ট: `helpdesk`) |
| `--provider openai\|deepseek` | LLM প্রোভাইডার |
| `--use-mcp` | in-process-এর বদলে স্থানীয় MCP সার্ভার থেকে টুল |
| `--no-mlflow` | demand-forecast-এ mock ML ট্র্যাকিং |
| `--stream` / `--no-stream` | চ্যাট টোকেন স্ট্রিমিং |
| `--stream-events` | গ্রাফ নোড আপডেট স্ট্রিম |

প্যাটার্ন-নির্দিষ্ট ফ্ল্যাগ (যেমন `--auto-approve`, `--time-travel`) প্রতিটি `example/README.bn.md`-তে।

---

## ১৫টি ডিজাইন প্যাটার্ন

| # | প্যাটার্ন | বিভাগ | সাধারণ সিনারিও |
|---|----------|-------|----------------|
| 01 | [ReAct](patterns/01-react/) | Core loop | যেকোনো টুল-ব্যবহারকারী এজেন্ট |
| 02 | [Tool Use](patterns/02-tool-use/) | Core loop | স্পষ্ট টুল রেজিস্ট্রি |
| 03 | [Planning](patterns/03-planning/) | Core loop | বহু-ধাপ ML পাইপলাইন |
| 04 | [Prompt Chaining](patterns/04-prompt-chaining/) | Workflow | নির্দিষ্ট পাইপলাইন |
| 05 | [Routing](patterns/05-routing/) | Workflow | VPN / email / order ইনটেন্ট |
| 06 | [Parallelization](patterns/06-parallelization/) | Workflow | FAQ + স্ট্যাটাস একসাথে |
| 07 | [Orchestrator–Workers](patterns/07-orchestrator-workers/) | Workflow | MLDLC বিশেষজ্ঞ |
| 08 | [Evaluator–Optimizer](patterns/08-evaluator-optimizer/) | Workflow | উত্তরের মান উন্নতি |
| 09 | [Human-in-the-Loop](patterns/09-human-in-the-loop/) | Control | টিকেট, রিফান্ড, মডেল অনুমোদন |
| 10 | [Memory](patterns/10-memory/) | Control | মাল্টি-টার্ন follow-up |
| 11 | [RAG](patterns/11-rag/) | Control | FAQ / playbook রিট্রিভাল |
| 12 | [Guardrails](patterns/12-guardrails/) | Control | PII ও নীতি যাচাই |
| 13 | [Handoff](patterns/13-handoff/) | Advanced | Tier-1 → Tier-2 |
| 14 | [Map–Reduce](patterns/14-map-reduce/) | Advanced | অনেক incident লগ সারসংক্ষেপ |
| 15 | [Event-Driven](patterns/15-event-driven/) | Advanced | ইনবাউন্ড ইমেইল / retrain |

সম্পূর্ণ ইনডেক্স: [patterns/README.bn.md](patterns/README.bn.md) · শব্দকোষ: [docs/bn/patterns/glossary.md](docs/bn/patterns/glossary.md)

**প্রস্তাবিত শেখার ক্রম:** 01 ReAct → 02 Tool Use → (11 RAG বা 05 Routing) → 09 HITL → 07 Orchestrator–Workers। বিস্তারিত [শুরু করা](docs/bn/getting-started.md)।

---

## প্রজেক্ট কাঠামো

```
agentic-ai-overview/
├── patterns/                 # ১৫টি নম্বরযুক্ত প্যাটার্ন ফোল্ডার
│   └── XX-name/
│       ├── README.bn.md      # প্যাটার্ন কী, কখন ব্যবহার
│       ├── use-case.bn.md    # সিনারিও বর্ণনা
│       └── example/          # graph.py + main.py
├── shared/                   # সিনারিও, CLI, LangGraph, MCP
├── docs/bn/                  # বাংলা ডকুমেন্টেশন
├── tests/
└── pyproject.toml
```

---

## ফ্রেমওয়ার্ক ও রানটাইম

সব উদাহরণ **[LangGraph](docs/bn/architecture/langgraph.md)** ব্যবহার করে।

| বৈশিষ্ট্য | কোথায় | নোট |
|----------|--------|------|
| **OpenAI & DeepSeek** | সব | `--provider openai\|deepseek` |
| **Chat streaming** | 01, 02 | helpdesk/ecommerce |
| **SQLite persistence** | 09, 10 | `data/checkpoints/` |
| **HITL interrupts** | 09 | side-effect টুলের আগে pause |
| **Time travel** | 09 | `--time-travel` |
| **Worker subgraphs** | 07 | MLDLC ওয়ার্কার |
| **Event streaming** | 07, 15 | `stream_mode="updates"` |
| **MCP tools** | সব (ঐচ্ছিক) | `--use-mcp` |
| **MLflow** | demand-forecast | `--no-mlflow` mock |

---

## উদাহরণ কমান্ড

```bash
python patterns/01-react/example/main.py --scenario helpdesk --provider deepseek
python patterns/09-human-in-the-loop/example/main.py --scenario helpdesk --auto-approve --time-travel
python patterns/07-orchestrator-workers/example/main.py --scenario demand-forecast --no-mlflow
pytest
```

---

## ডকুমেন্টেশন মানচিত্র

| ডক | উদ্দেশ্য |
|----|---------|
| [শুরু করা](docs/bn/getting-started.md) | শেখার পথ |
| [English documentation](docs/getting-started.md) | ইংরেজি ডক |
| [LangGraph](docs/bn/architecture/langgraph.md) | গ্রাফ, ক্ষমতা, প্যাটার্ন ম্যাপিং |
| [Single vs multi-agent](docs/bn/architecture/single-vs-multi-agent.md) | আর্কিটেকচার বেছে নেওয়া |
| [MCP](docs/bn/architecture/mcp.md) | MCP টুল ট্রান্সপোর্ট |
| [সব উদাহরণ চালান](docs/bn/use-cases/run-all-examples.md) | কপি-পেস্ট কমান্ড |

---

## লাইসেন্স

[LICENSE](LICENSE) দেখুন।
