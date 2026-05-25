> [English](README.md) | **বাংলা**

# Map–Reduce

## এটি কী

**Map:** chunk-এ split, parallel process। **Reduce:** partial merge → final output।

## কখন ব্যবহার

- long document/log summarize।
- token limit — chunking দরকার।

## সম্পর্কিত

- [Parallelization](../06-parallelization/), [Prompt Chaining](../04-prompt-chaining/)

## উদাহরণ

`python patterns/14-map-reduce/example/main.py` — incident batch → executive report
