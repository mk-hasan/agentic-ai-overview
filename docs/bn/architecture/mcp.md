> [English](mcp.md) | **বাংলা**

# MCP টুল সার্ভার (ঐচ্ছিক)

ডিফল্টে টুল **in-process** লোড হয়। **`--use-mcp`** দিলে একই সিনারিও টুল **stdio MCP**-তে সerv হয় এবং [langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters) দিয়ে লোড হয়।

প্রোডাকশনে এজেন্ট часто Python import-এর বদলে আলাদা MCP সার্ভারে টুল কল করে — এটা সেই setup-এর prototype।

## প্রয়োজনীয়তা

- **Python 3.10+** (`mcp` SDK 3.9-এ নেই)
- `pip install -r requirements-mcp.txt`

## ব্যবহার

```bash
pip install -r requirements-mcp.txt

python patterns/01-react/example/main.py --scenario helpdesk --use-mcp --provider openai
python patterns/07-orchestrator-workers/example/main.py --scenario demand-forecast --use-mcp --no-mlflow
```

`.env`-এ:

```bash
USE_MCP=1
```

## কীভাবে কাজ করে

1. **`shared/examples/tool_provider.py`** — `USE_MCP` অনুযায়ী local বা MCP।
2. **`shared/mcp/server.py`** — FastMCP; `--scenario` অনুযায়ী টুল।
3. **`shared/mcp/client.py`** — subprocess সার্ভার, LangChain-compatible টুল।

গ্রাফের আচরণ বদলায় না — শুধু টুল transport।

## MCP কখন

| Local (ডিফল্ট) | MCP |
|----------------|-----|
| শেখার জন্য দ্রুততম | বাহ্যিক টুল সার্ভারের মতো |
| extra dep নেই | subprocess isolation |
| Python 3.9 OK | Python 3.10+ |

Cursor, Claude Desktop, বা নিজের MCP সার্ভিসের সাথে prototype-এ MCP ব্যবহার করুন।
