# Map–Reduce Example (LangGraph)

Summarize many helpdesk incident records in parallel, then merge into one executive report.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/14-map-reduce/example/main.py
python patterns/14-map-reduce/example/main.py --provider openai
```

## What it demonstrates

- Map phase produces one summary per incident from sample JSON data
- Reduce phase synthesizes partial summaries into a final executive report
- Scales narrative analysis beyond a single prompt’s context window
