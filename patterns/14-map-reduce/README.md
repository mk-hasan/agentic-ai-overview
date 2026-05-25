> **English** | [বাংলা](README.bn.md)

# Map–Reduce

## What it is

**Map:** split input into chunks and process independently (often in parallel). **Reduce:** merge partial results into a final output. Scales to large inputs.

## When to use it

- Summarizing long documents, books, or log dumps.
- Per-item analysis over large lists with aggregate report.
- Token limits require chunking.

## When not to use it

- Global context across entire input is required in one pass.
- Reduce step is ill-defined for your domain.

## Related patterns

- [Parallelization](../06-parallelization/) — map phase is typically parallel
- [Prompt Chaining](../04-prompt-chaining/) — reduce may be a chain of merges

## Example

See [`example/`](example/) — **LangGraph map–reduce demo** (IT helpdesk: batch incident summaries → executive report).

Run from repo root: `python patterns/14-map-reduce/example/main.py`

## Real-life use case

See [`use-case.md`](use-case.md).

**Suggested domains:** Earnings call transcript summary, codebase-wide security scan report, survey theme extraction.
