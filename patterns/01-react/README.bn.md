> [English](README.md) | **বাংলা**

# ReAct (Reason + Act)

## এটি কী

এজেন্ট **যুক্তি** (পরবর্তী ধাপ পরিকল্পনা) ও **কাজ** (টুল/API) এর মধ্যে বদলায়, **পর্যবেক্ষণ** করে, লক্ষ্য না হওয়া পর্যন্ত পুনরাবৃত্তি।

## কখন ব্যবহার

- অনেক ধাপ, বাহ্যিক feedback (search, API)।
- ধাপে ধাপে ব্যাখ্যাযোগ্য আচরণ।
- টুল-ব্যবহারকারী এজেন্টের ডিফল্ট লুপ।

## কখন নয়

- এক-shot Q&A, টুল নেই।
- কঠোর latency — planning overhead বেশি।

## কাঠামো

```
Thought → Action → Observation → Thought → … → Final Answer
```

## সম্পর্কিত প্যাটার্ন

- [Tool Use](../02-tool-use/)
- [Planning](../03-planning/)
- [Evaluator–Optimizer](../08-evaluator-optimizer/)

## উদাহরণ

[`example/`](example/) — LangGraph ReAct (IT helpdesk: FAQ + ticket)।

`python patterns/01-react/example/main.py`

## বাস্তব use case

[`use-case.bn.md`](use-case.bn.md) — [IT Helpdesk](../../docs/bn/use-cases/it-helpdesk.md)।
