> [English](README.md) | **বাংলা**

# Human-in-the-Loop (HITL)

## এটি কী

অপরিবর্তনীয়/ঝুঁকিপূর্ণ কাজের **আগে মানুষের approve/input/correction** — checkpoint-এ pause।

## কখন ব্যবহার

- financial, medical, production deploy।
- regulatory, low model trust।

## সম্পর্কিত

- [Guardrails](../12-guardrails/), [Evaluator–Optimizer](../08-evaluator-optimizer/), [Tool Use](../02-tool-use/)

## উদাহরণ

`python patterns/09-human-in-the-loop/example/main.py` — `--auto-approve`, `--time-travel`
