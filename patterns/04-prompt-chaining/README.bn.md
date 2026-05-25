> [English](README.md) | **বাংলা**

# Prompt Chaining

## এটি কী

**নির্দিষ্ট LLM ধাপের ধারা** — প্রতিটি output পরের input; dynamic branching নেই।

## কখন ব্যবহার

- extract → transform → summarize।
- প্রতি stage আলাদা prompt, সহজ test/observe।

## কখন নয়

- intermediate result অনুযায়ী path ([Routing](../05-routing/))।
- parallel speed ([Parallelization](../06-parallelization/))।

## উদাহরণ

`python patterns/04-prompt-chaining/example/main.py`
