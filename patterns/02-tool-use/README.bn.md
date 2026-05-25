> [English](README.md) | **বাংলা**

# Tool Use / Function Calling

## এটি কী

মডেল **ঘোষিত টুল** থেকে বেছে structured arguments দেয়; runtime টুল চালিয়ে ফল মডেলে ফেরত দেয়।

## কখন ব্যবহার

- লাইভ ডেটা (CRM, ticket)।
- side effect: email, ticket, query।
- ReAct/planner-এ structured action।

## কখন নয়

- শুধু টেক্সট জেনারেশন।
- unstable tool schema।

## সম্পর্কিত

- [ReAct](../01-react/), [Routing](../05-routing/), [Guardrails](../12-guardrails/)

## উদাহরণ

[`example/`](example/) — `python patterns/02-tool-use/example/main.py`

[`use-case.bn.md`](use-case.bn.md)
