"""MCP server exposing scenario tools (stdio). Run via langchain-mcp-adapters client."""

import argparse
import functools
import os
import sys
from pathlib import Path

# Ensure repo root is importable when launched as a subprocess.
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from mcp.server.fastmcp import FastMCP

from shared.examples.scenarios import get_scenario


def register_langchain_tool(mcp: FastMCP, lc_tool) -> None:
    """Expose a LangChain tool on the MCP server with its native signature."""
    underlying = getattr(lc_tool, "func", None) or getattr(lc_tool, "coroutine", None)
    description = lc_tool.description or lc_tool.name

    if underlying is None:

        def handler(**kwargs):
            return lc_tool.invoke(kwargs)

        handler.__name__ = lc_tool.name.replace("-", "_")
        handler.__doc__ = description
        mcp.tool(name=lc_tool.name, description=description)(handler)
        return

    @functools.wraps(underlying)
    def wrapped(*args, **kwargs):
        return underlying(*args, **kwargs)

    wrapped.__name__ = lc_tool.name.replace("-", "_")
    mcp.tool(name=lc_tool.name, description=description)(wrapped)


def build_mcp_server(scenario: str) -> FastMCP:
    sc = get_scenario(scenario)
    mcp = FastMCP(f"agentic-ai-{scenario}")

    for tool in sc.get_extended_tools():
        register_langchain_tool(mcp, tool)

    return mcp


def main() -> None:
    parser = argparse.ArgumentParser(description="Agentic AI overview MCP tool server")
    parser.add_argument(
        "--scenario",
        required=True,
        choices=["helpdesk", "ecommerce", "demand-forecast"],
        help="Which use-case tool set to expose",
    )
    args = parser.parse_args()
    os.environ.setdefault("SCENARIO", args.scenario)
    server = build_mcp_server(args.scenario)
    server.run(transport="stdio")


if __name__ == "__main__":
    main()
