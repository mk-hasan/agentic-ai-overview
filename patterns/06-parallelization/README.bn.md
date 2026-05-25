> [English](README.md) | **বাংলা**

# Parallelization

## এটি কী

**স্বাধীন উপ-কাজ সমান্তরাল**, তারপর merge — latency কমায় parallel কাজে।

## কখন ব্যবহার

- অনেক document summarize, একসাথে API।
- fan-out research।

## কখন নয়

- sequential dependency।
- strict token budget — cost গুণ হয়।

## সম্পর্কিত

- [Map–Reduce](../14-map-reduce/), [Orchestrator–Workers](../07-orchestrator-workers/)

## উদাহরণ

`python patterns/06-parallelization/example/main.py`
