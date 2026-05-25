"""Handoff — Tier-1 escalates complex cases to Tier-2."""

from typing import Annotated, TypedDict

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_core_tools, get_extended_tools, get_tool_catalog, get_tools_by_name, get_tool_by_name
from shared.utils.llm import get_chat_model


class HandoffState(TypedDict):
    messages: Annotated[list, add_messages]
    user_request: str
    tier: str


def _tier_agent(provider: str, tools: list, system: str):
    model = get_chat_model(provider=provider).bind_tools(tools)

    def node(state: HandoffState):
        msgs = [SystemMessage(content=system), HumanMessage(content=state["user_request"])] + state[
            "messages"
        ]
        return {"messages": [model.invoke(msgs)]}

    return node


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk"):
    s = get_scenario(scenario)
    tier1_tools = get_tools_by_name(scenario, s.tier1_tool_names)
    tier2_tools = get_tools_by_name(scenario, s.tier2_tool_names)
    tier1_agent = _tier_agent(provider, tier1_tools, s.tier1_prompt)
    tier2_agent = _tier_agent(provider, tier2_tools, s.tier2_prompt)
    tier1_tool_node = ToolNode(tier1_tools)
    tier2_tool_node = ToolNode(tier2_tools)
    classifier = get_chat_model(provider=provider)

    def tier1(state: HandoffState):
        return {"tier": "tier1", **tier1_agent(state)}

    def run_tier1_tools(state: HandoffState):
        return tier1_tool_node.invoke(state)

    def assess_handoff(state: HandoffState):
        r = classifier.invoke(
            [
                SystemMessage(content=s.handoff_escalation_prompt),
                HumanMessage(content=str(state["messages"][-3:])),
            ]
        )
        if "yes" in r.content.lower():
            return {
                "tier": "tier2",
                "messages": [AIMessage(content="Handoff: escalating to Tier-2 specialist.")],
            }
        return {"tier": "done"}

    def tier2(state: HandoffState):
        return tier2_agent(state)

    def run_tier2_tools(state: HandoffState):
        return tier2_tool_node.invoke(state)

    def route_tier1_tools(state: HandoffState):
        last = state["messages"][-1]
        if getattr(last, "tool_calls", None):
            return "tier1_tools"
        return "assess"

    def route_tier2_tools(state: HandoffState):
        last = state["messages"][-1]
        if getattr(last, "tool_calls", None):
            return "tier2_tools"
        return END

    def route_after_assess(state: HandoffState):
        return "tier2" if state.get("tier") == "tier2" else END

    graph = StateGraph(HandoffState)
    graph.add_node("tier1", tier1)
    graph.add_node("tier1_tools", run_tier1_tools)
    graph.add_node("assess", assess_handoff)
    graph.add_node("tier2", tier2)
    graph.add_node("tier2_tools", run_tier2_tools)
    graph.add_edge(START, "tier1")
    graph.add_conditional_edges("tier1", route_tier1_tools, {"tier1_tools": "tier1_tools", "assess": "assess"})
    graph.add_edge("tier1_tools", "tier1")
    graph.add_conditional_edges("assess", route_after_assess, {"tier2": "tier2", END: END})
    graph.add_conditional_edges("tier2", route_tier2_tools, {"tier2_tools": "tier2_tools", END: END})
    graph.add_edge("tier2_tools", "tier2")
    return graph.compile()
