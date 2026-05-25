"""LangGraph ReAct loop: agent node ↔ tool node until done."""

from shared.examples.graphs.react import build_react_graph
from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_core_tools, get_extended_tools, get_tool_catalog, get_tools_by_name, get_tool_by_name


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk"):
    s = get_scenario(scenario)
    return build_react_graph(provider=provider, tools=get_core_tools(scenario))


def get_system_prompt(scenario: str = "helpdesk") -> str:
    s = get_scenario(scenario)
    return s.base_system_prompt + s.react_suffix
