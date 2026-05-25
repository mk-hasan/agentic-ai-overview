> [English](../getting-started.md) | **বাংলা**

# শুরু করা

ডক পড়ার এবং **প্রথম উদাহরণ** তৈরির প্রস্তাবিত ক্রম। দরকারি কিছু পাঠানোর আগে ১৫টি প্যাটার্ন সব শেষ করতে হবে না — ছোট থেকে শুরু করুন, use case অনুযায়ী প্যাটার্ন যোগ করুন।

## কোডের আগে (১৫ মিনিট)

1. [Single-agent বনাম multi-agent](architecture/single-vs-multi-agent.md) — আর্কিটেকচার বেছে নিন (ডিফল্ট: **single-agent**)।
2. [প্যাটার্ন ইনডেক্স](patterns/README.md) — কী কী আছে এক নজরে দেখুন।
3. editable মোডে ইনস্টল ও env কপি:
   ```bash
   pip install -e .
   cp .env.example .env
   ```
4. [LangGraph কনভেনশন](architecture/langgraph.md) পড়ুন — সব উদাহরণ LangGraph ব্যবহার করে।

## প্রথম প্যাটার্ন: এখান থেকে

### ১. [ReAct](../../patterns/01-react/) — **সবসময় প্রথম**

ReAct টুল-ব্যবহারকারী এজেন্টের ডিফল্ট লুপ: **চিন্তা → কাজ → পর্যবেক্ষণ → পুনরাবৃত্তি**।

কেন প্রথম:
- অন্যান্য single-agent প্যাটার্ন এ লুপের উপর ভিত্তি করে।
- ডিবাগ সহজ (প্রতিটি ধাপ দৃশ্যমান)।
- বেশিরভাগ ফ্রেমওয়ার্ক একইভাবে এজেন্ট গঠন করে।

**প্রথম উদাহরণ:** IT হেল্পডেস্ক বট — FAQ খুঁজে, প্রয়োজনে টিকেট খোলে।

চালান:

```bash
python patterns/01-react/example/main.py --provider openai
python patterns/01-react/example/main.py --provider deepseek
```

---

### ২. [Tool Use](../../patterns/02-tool-use/) — **দ্বিতীয়**

ReAct ছাড়া টুল = শুধু chain-of-thought। টুল = এজেন্ট **কাজ** করে।

---

### ৩. use case অনুযায়ী একটি শাখা

| প্রয়োজন | পরবর্তী প্যাটার্ন | ফোল্ডার |
|---------|-------------------|---------|
| কোম্পানির ডক / নীতি | RAG | [11-rag](../../patterns/11-rag/) |
| অনেক ধাপ, পরিকল্পনা | Planning | [03-planning](../../patterns/03-planning/) |
| উত্তরের মান | Evaluator–Optimizer | [08-evaluator-optimizer](../../patterns/08-evaluator-optimizer/) |
| নির্দিষ্ট পাইপলাইন | Prompt Chaining | [04-prompt-chaining](../../patterns/04-prompt-chaining/) |
| ভিন্ন ইনটেন্ট → ভিন্ন হ্যান্ডলার | Routing | [05-routing](../../patterns/05-routing/) |
| নিরাপত্তা / compliance | Guardrails | [12-guardrails](../../patterns/12-guardrails/) |
| কাজের আগে অনুমোদন | Human-in-the-Loop | [09-human-in-the-loop](../../patterns/09-human-in-the-loop/) |

---

### ৪. Multi-agent — **কাজ করা single-agent এর পর**

যখন এক এজেন্টের prompt ও টুল খুব বড়, বা স্পষ্ট ভূমিকা দরকার:

1. [Orchestrator–Workers](../../patterns/07-orchestrator-workers/)
2. [Handoff](../../patterns/13-handoff/) — কথোপকথনের মাঝে নিয়ন্ত্রণ হস্তান্তর

---

## প্রস্তাবিত শেখার পথ

```
পর্ব ১ — ভিত্তি (single-agent)
  01 ReAct  →  02 Tool Use  →  03 Planning

পর্ব ২ — মান ও জ্ঞান
  11 RAG  →  08 Evaluator–Optimizer  →  12 Guardrails

পর্ব ৩ — ওয়ার্কফ্লো
  04 Prompt Chaining  →  05 Routing  →  06 Parallelization

পর্ব ৪ — Multi-agent
  07 Orchestrator–Workers  →  13 Handoff  →  14 Map–Reduce

পর্ব ৫ — প্রোডাকশন
  09 Human-in-the-Loop  →  10 Memory  →  15 Event-Driven
```

---

## প্রতি প্যাটার্নে কাজের ধারা

1. প্যাটার্ন `README.bn.md` পড়ুন
2. `use-case.bn.md` পূরণ করুন
3. `example/`-তে বাস্তবায়ন
4. `example/README.bn.md`-তে রান ধাপ লিখুন

[`templates/pattern-example/`](../../templates/pattern-example/) কপি করে scaffold নিতে পারেন।

---

## দ্রুত সিদ্ধান্ত: “আজ কোন ফোল্ডার?”

| আপনি… | খুলুন |
|-------|-------|
| এজেন্টিক AI-তে নতুন | [patterns/01-react/](../../patterns/01-react/) |
| ReAct আছে, API দরকার | [patterns/02-tool-use/](../../patterns/02-tool-use/) |
| টুল আছে, অভ্যন্তরীণ ডক দরকার | [patterns/11-rag/](../../patterns/11-rag/) |
| একাধিক বিশেষজ্ঞ এজেন্ট | [patterns/07-orchestrator-workers/](../../patterns/07-orchestrator-workers/) |
| নিশ্চিত নন | [patterns/01-react/](../../patterns/01-react/) |
