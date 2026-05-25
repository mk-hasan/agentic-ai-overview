> [English](README.md) | **বাংলা**

# Memory & Context Management

## এটি কী

**কথোপকথন, preference, session state** persist/retrieve — turn ও session জুড়ে coherent।

## কখন ব্যবহার

- multi-turn assistant, ongoing project।
- personalization, prior decision recall।

## সম্পর্কিত

- [RAG](../11-rag/), [Planning](../03-planning/)

## উদাহরণ

`python patterns/10-memory/example/main.py` — SQLite checkpoint + `thread_id`
