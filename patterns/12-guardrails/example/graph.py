"""Guardrails — input/output policy checks around the agent."""

from typing import Annotated, TypedDict

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from shared.examples.helpdesk.guardrails import scan_for_pii, scan_for_policy_violations
from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_core_tools, get_extended_tools, get_tool_catalog, get_tools_by_name, get_tool_by_name
from shared.utils.llm import get_chat_model


class GuardState(TypedDict):
    messages: Annotated[list, add_messages]
    user_request: str
    blocked_reason: str


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk"):
    s = get_scenario(scenario)
    tools = get_core_tools(scenario)
    model = get_chat_model(provider=provider).bind_tools(tools)
    tool_node = ToolNode(tools)

    def input_guard(state: GuardState):
        pii = scan_for_pii(state["user_request"])
        violations = scan_for_policy_violations(state["user_request"])
        if pii:
            return {
                "blocked_reason": f"PII detected: {', '.join(pii)}",
                "messages": [AIMessage(content="Please remove sensitive personal data and retry.")],
            }
        if violations:
            return {
                "blocked_reason": f"Policy violation: {', '.join(violations)}",
                "messages": [AIMessage(content="That request cannot be processed due to security policy.")],
            }
        return {"blocked_reason": "", "messages": [HumanMessage(content=state["user_request"])]}

    def agent(state: GuardState):
        msgs = [SystemMessage(content=s.base_system_prompt)] + state["messages"]
        return {"messages": [model.invoke(msgs)]}

    def run_tools(state: GuardState):
        return tool_node.invoke(state)

    def output_guard(state: GuardState):
        text = state["messages"][-1].content or ""
        if scan_for_pii(text):
            return {
                "messages": [
                    AIMessage(content="[Guardrail] Response withheld — potential sensitive data detected.")
                ]
            }
        return {}

    def route_after_input(state: GuardState):
        return END if state.get("blocked_reason") else "agent"

    def route_after_agent(state: GuardState):
        last = state["messages"][-1]
        if getattr(last, "tool_calls", None):
            return "tools"
        return "output_guard"

    graph = StateGraph(GuardState)
    graph.add_node("input_guard", input_guard)
    graph.add_node("agent", agent)
    graph.add_node("tools", run_tools)
    graph.add_node("output_guard", output_guard)
    graph.add_edge(START, "input_guard")
    graph.add_conditional_edges("input_guard", route_after_input, {END: END, "agent": "agent"})
    graph.add_conditional_edges("agent", route_after_agent, {"tools": "tools", "output_guard": "output_guard"})
    graph.add_edge("tools", "agent")
    graph.add_edge("output_guard", END)
    return graph.compile()
