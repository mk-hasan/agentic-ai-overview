> [English](README.md) | **বাংলা**

# Planning & Task Decomposition

## এটি কী

কাজের **উপ-কাজে ভাঙা** (plan), ক্রমে execution — ব্যর্থ হলে replan।

## কখন ব্যবহার

- বহু-ধাপ প্রজেক্ট, dependency গুরুত্বপূর্ণ।
- wasted tool call কমাতে upfront structure।

## কখন নয়

- এক-টুল lookup।
- plan দ্রুত stale হয় এমন environment।

## সম্পর্কিত

- [ReAct](../01-react/), [Orchestrator–Workers](../07-orchestrator-workers/), [Map–Reduce](../14-map-reduce/)

## উদাহরণ

`python patterns/03-planning/example/main.py` — [`use-case.bn.md`](use-case.bn.md)
