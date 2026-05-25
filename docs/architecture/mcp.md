# MCP tool server (optional)

Examples load tools **in-process** by default. With **`--use-mcp`**, the same scenario tools are served over **stdio MCP** and loaded via [langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters).

This mirrors production setups where agents call tools on separate MCP servers instead of importing Python modules directly.

## Requirements

- **Python 3.10+** (the official `mcp` SDK does not support 3.9)
- Extra deps: `pip install -r requirements-mcp.txt`

## Usage

```bash
pip install -r requirements-mcp.txt

# Same examples, tools via MCP subprocess
python patterns/01-react/example/main.py --scenario helpdesk --use-mcp --provider openai
python patterns/02-tool-use/example/main.py --scenario ecommerce --use-mcp
python patterns/07-orchestrator-workers/example/main.py --scenario demand-forecast --use-mcp --no-mlflow
```

Or set in `.env`:

```bash
USE_MCP=1
```

## How it works

```mermaid
flowchart LR
  main[example/main.py] --> cli[--use-mcp sets USE_MCP]
  cli --> graph[pattern graph.py]
  graph --> tp[tool_provider.py]
  tp -->|USE_MCP=0| local[scenario tools.py]
  tp -->|USE_MCP=1| client[shared/mcp/client.py]
  client -->|stdio| server[shared/mcp/server.py]
  server --> local
```

1. **`shared/examples/tool_provider.py`** — same API as scenario tools (`get_core_tools`, `get_extended_tools`, …) but switches on `USE_MCP`.
2. **`shared/mcp/server.py`** — FastMCP server; registers all extended tools for the chosen `--scenario`.
3. **`shared/mcp/client.py`** — spawns the server as a subprocess and returns LangChain-compatible tools for LangGraph.

Graphs do not change behavior—only the tool transport.

## Run the server standalone (debug)

```bash
python shared/mcp/server.py --scenario helpdesk
```

The server speaks MCP over stdio; use an MCP inspector or the LangChain client to connect.

## When to use MCP

| Local tools (default) | MCP (`--use-mcp`) |
|----------------------|-------------------|
| Fastest for learning | Matches external tool servers |
| No extra deps | Tools isolated in subprocess |
| Python 3.9 OK | Requires Python 3.10+ |

Use MCP when prototyping integrations with Cursor, Claude Desktop, or your own MCP-hosted services.
