"""Tool Use pattern — explicit tool registry + bound ReAct agent."""

from shared.examples.graphs.react import build_react_graph
from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import (
    get_core_tools,
    get_extended_tools,
    get_tool_catalog as fetch_tool_catalog,
    get_tools_by_name,
    get_tool_by_name,
)


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk"):
    s = get_scenario(scenario)
    tools = get_extended_tools(scenario)
    return build_react_graph(provider=provider, tools=tools), tools


def get_tool_catalog(scenario: str = "helpdesk") -> dict:
    return fetch_tool_catalog(scenario)
