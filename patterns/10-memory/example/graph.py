"""Memory — multi-turn helpdesk with checkpointed conversation."""

from shared.examples.graphs.react import build_react_graph
from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_core_tools
from shared.langgraph.checkpointer import get_checkpointer


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk", sqlite: bool = True):
    s = get_scenario(scenario)
    return build_react_graph(
        provider=provider,
        tools=get_core_tools(scenario),
        checkpointer=get_checkpointer(sqlite=sqlite),
    )


def get_system_prompt(scenario: str = "helpdesk") -> str:
    s = get_scenario(scenario)
    return s.base_system_prompt + """

Remember prior turns in this thread. If the user refers to earlier issues, use that context."""
