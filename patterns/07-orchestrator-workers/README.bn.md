> [English](README.md) | **বাংলা**

# Orchestrator–Workers (Multi-Agent)

## এটি কী

**কেন্দ্রীয় orchestrator** কাজ ভেঙে **বিশেষজ্ঞ worker**-দের দেয়; synthesize করে unified output।

## কখন ব্যবহার

- legal + finance + engineering একসাথে।
- role boundary ও audit trail।
- monolithic prompt-এ ধরা যায় না এমন কাজ।

## সম্পর্কিত

- [Planning](../03-planning/), [Handoff](../13-handoff/), [Parallelization](../06-parallelization/)

## উদাহরণ

`python patterns/07-orchestrator-workers/example/main.py` — supervisor + VPN/identity/email specialists।
