"""Unified tool loading: local LangChain tools or optional MCP server."""

import os
from typing import List, Optional

from shared.examples.scenarios import get_scenario


def is_mcp_enabled() -> bool:
    return os.getenv("USE_MCP", "0").strip().lower() in ("1", "true", "yes", "on")


def set_mcp_enabled(enabled: bool) -> None:
    os.environ["USE_MCP"] = "1" if enabled else "0"


def _local_extended(scenario: str) -> List:
    return get_scenario(scenario).get_extended_tools()


def _local_core(scenario: str) -> List:
    return get_scenario(scenario).get_core_tools()


def _filter_by_names(tools: List, names: List[str]) -> List:
    wanted = set(names)
    return [t for t in tools if t.name in wanted]


def get_extended_tools(scenario: str, *, use_mcp: Optional[bool] = None) -> List:
    use_mcp = is_mcp_enabled() if use_mcp is None else use_mcp
    if not use_mcp:
        return _local_extended(scenario)
    from shared.mcp.client import load_mcp_tools

    return load_mcp_tools(scenario)


def get_core_tools(scenario: str, *, use_mcp: Optional[bool] = None) -> List:
    use_mcp = is_mcp_enabled() if use_mcp is None else use_mcp
    if not use_mcp:
        return _local_core(scenario)
    core_names = [t.name for t in _local_core(scenario)]
    return _filter_by_names(get_extended_tools(scenario, use_mcp=True), core_names)


def get_tools_by_name(scenario: str, names: List[str], *, use_mcp: Optional[bool] = None) -> List:
    tools = get_extended_tools(scenario, use_mcp=use_mcp)
    by_name = {t.name: t for t in tools}
    return [by_name[n] for n in names if n in by_name]


def get_tool_catalog(scenario: str, *, use_mcp: Optional[bool] = None) -> dict:
    if not (use_mcp if use_mcp is not None else is_mcp_enabled()):
        return get_scenario(scenario).get_tool_catalog()
    return {t.name: (t.description or t.name) for t in get_extended_tools(scenario, use_mcp=True)}


def get_tool_by_name(scenario: str, name: str, *, use_mcp: Optional[bool] = None):
    matches = get_tools_by_name(scenario, [name], use_mcp=use_mcp)
    if not matches:
        raise KeyError(name)
    return matches[0]
