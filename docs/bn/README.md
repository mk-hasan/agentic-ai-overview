> [English](../README.md) | **বাংলা**

# বাংলা ডকুমেন্টেশন

এই ফোল্ডারে প্রজেক্ট ডকুমেন্টেশনের বাংলা অনুবাদ। কোড, কমান্ড, ফাইল পাথ ও API নাম ইংরেজিতেই থাকে।

## শুরু

| ডক | বিষয় |
|----|-------|
| [README.bn.md](../../README.bn.md) | প্রজেক্ট ওভারভিউ |
| [getting-started.md](getting-started.md) | শেখার পথ ও প্রথম উদাহরণ |

## আর্কিটেকচার

| ডক | বিষয় |
|----|-------|
| [overview.md](architecture/overview.md) | প্রজেক্ট কাঠামো ও কনভেনশন |
| [langgraph.md](architecture/langgraph.md) | LangGraph, providers, capabilities |
| [single-vs-multi-agent.md](architecture/single-vs-multi-agent.md) | Single vs multi-agent |
| [mcp.md](architecture/mcp.md) | MCP টুল সার্ভার |
| [Production architecture](../../architecture/production/README.md) | প্রোডাকশন ডিপ্লয় গাইড (ইংরেজি) |

## প্যাটার্ন ও use cases

| ডক | বিষয় |
|----|-------|
| [patterns/README.md](patterns/README.md) | ১৫টি প্যাটার্ন ইনডেক্স |
| [patterns/glossary.md](patterns/glossary.md) | শব্দকোষ |
| [use-cases/README.md](use-cases/README.md) | তিনটি সিনারিও |
| [use-cases/it-helpdesk.md](use-cases/it-helpdesk.md) | IT হেল্পডেস্ক |
| [use-cases/ecommerce-order-support.md](use-cases/ecommerce-order-support.md) | ই-কমার্স |
| [use-cases/demand-forecast.md](use-cases/demand-forecast.md) | ML পাইপলাইন |
| [use-cases/run-all-examples.md](use-cases/run-all-examples.md) | সব রান কমান্ড |

## প্যাটার্ন ফোল্ডার

প্রতিটি `patterns/XX-name/`-এ:

- `README.bn.md` — প্যাটার্ন বর্ণনা
- `use-case.bn.md` — IT helpdesk সিনারিও
- `example/README.bn.md` — উদাহরণ চালানো
- `example/{helpdesk,ecommerce,demand-forecast}/README.bn.md` — সিনারিও shortcut

[patterns/README.bn.md](../../patterns/README.bn.md) থেকে সব প্যাটার্নে যান।

## অনুবাদ তৈরি / আপডেট

```bash
python scripts/generate_bn_docs.py
```

প্যাটার্ন `README.bn.md`, `use-case.bn.md`, এবং example README.bn.md ফাইলগুলো regenerate করে। মূল `docs/bn/` ফাইলগুলো হাতে সম্পাদিত।
