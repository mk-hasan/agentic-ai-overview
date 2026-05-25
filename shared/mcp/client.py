"""Load LangChain tools from a local MCP server (stdio)."""

import asyncio
import os
import sys
from functools import lru_cache
from typing import List

from shared.config.settings import REPO_ROOT

MIN_PYTHON = (3, 10)


def _require_python() -> None:
    if sys.version_info < MIN_PYTHON:
        raise RuntimeError(
            "MCP support requires Python 3.10+. "
            "Use local tools (default) or upgrade Python for --use-mcp."
        )


def mcp_server_script() -> str:
    return str(REPO_ROOT / "shared" / "mcp" / "server.py")


def _server_env(scenario: str) -> dict:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(REPO_ROOT) + os.pathsep + env.get("PYTHONPATH", "")
    env["SCENARIO"] = scenario
    return env


async def _load_tools_async(scenario: str) -> List:
    from langchain_mcp_adapters.client import MultiServerMCPClient

    client = MultiServerMCPClient(
        {
            scenario: {
                "transport": "stdio",
                "command": sys.executable,
                "args": [mcp_server_script(), "--scenario", scenario],
                "env": _server_env(scenario),
            }
        }
    )
    return await client.get_tools()


@lru_cache(maxsize=8)
def load_mcp_tools(scenario: str) -> List:
    """Load tools exposed by the repo MCP server for a scenario."""
    _require_python()
    try:
        return asyncio.run(_load_tools_async(scenario))
    except ImportError as exc:
        raise RuntimeError(
            "MCP client dependencies missing. Install with: pip install -r requirements-mcp.txt"
        ) from exc
