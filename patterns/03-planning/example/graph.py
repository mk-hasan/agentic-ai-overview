"""Planning pattern — plan steps, then execute each with tools."""

import re
from typing import Annotated, TypedDict

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_core_tools, get_extended_tools, get_tool_catalog, get_tools_by_name, get_tool_by_name
from shared.utils.llm import get_chat_model


class PlanState(TypedDict):
    messages: Annotated[list, add_messages]
    plan: list
    step_index: int
    user_request: str


def _parse_plan(text: str, fallback: list) -> list:
    lines = []
    for line in text.splitlines():
        line = re.sub(r"^\s*\d+[\).\-\s]+", "", line).strip()
        if line:
            lines.append(line)
    return lines[:8] or list(fallback)


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk"):
    s = get_scenario(scenario)
    base_prompt = s.base_system_prompt
    tools = get_core_tools(scenario)
    planner_model = get_chat_model(provider=provider)
    executor_model = get_chat_model(provider=provider).bind_tools(tools)
    tool_node = ToolNode(tools)

    def plan_node(state: PlanState):
        prompt = [
            SystemMessage(
                content=base_prompt
                + "\nCreate a numbered plan (3-8 steps) for this request. One step per line."
            ),
            HumanMessage(content=state["user_request"]),
        ]
        response = planner_model.invoke(prompt)
        plan = _parse_plan(response.content, s.plan_fallback_steps)
        if not plan:
            plan = list(s.plan_fallback_steps)
        return {
            "plan": plan,
            "step_index": 0,
            "messages": [AIMessage(content="Plan:\n" + "\n".join(f"{i+1}. {s}" for i, s in enumerate(plan)))],
        }

    def execute_step(state: PlanState):
        step = state["plan"][state["step_index"]]
        prompt = [
            SystemMessage(
                content=base_prompt
                + f"\nExecute ONLY this plan step: {step}\nUse tools when needed."
            ),
            HumanMessage(content=state["user_request"]),
        ] + state["messages"]
        response = executor_model.invoke(prompt)
        return {"messages": [response]}

    def run_tools(state: PlanState):
        return tool_node.invoke(state)

    def after_tools(state: PlanState):
        return {"step_index": state["step_index"] + 1}

    def route_after_agent(state: PlanState):
        last = state["messages"][-1]
        if getattr(last, "tool_calls", None):
            return "tools"
        if state["step_index"] + 1 < len(state["plan"]):
            return "next_step"
        return END

    graph = StateGraph(PlanState)
    graph.add_node("plan", plan_node)
    graph.add_node("execute", execute_step)
    graph.add_node("tools", run_tools)
    graph.add_node("advance", after_tools)
    graph.add_edge(START, "plan")
    graph.add_edge("plan", "execute")
    graph.add_conditional_edges("execute", route_after_agent, {"tools": "tools", "next_step": "advance", END: END})
    graph.add_edge("tools", "advance")
    graph.add_edge("advance", "execute")
    return graph.compile()
