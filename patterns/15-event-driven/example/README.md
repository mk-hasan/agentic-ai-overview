# Event-Driven Example (LangGraph)

Process an inbound support email event and generate an asynchronous IT helpdesk response.

## Run

From the repo root (after `pip install -r requirements.txt` and `.env` setup):

```bash
python patterns/15-event-driven/example/main.py
python patterns/15-event-driven/example/main.py --provider deepseek
```

## What it demonstrates

- Workflow triggered by a structured email event (from, subject, body)
- Agent triages the parsed request and drafts a reply outside live chat
- Output shaped for mailer or ticketing integration rather than console chat
