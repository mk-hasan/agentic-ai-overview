"""Human-in-the-Loop — manager approval before side-effect actions."""

import json
from typing import Annotated, TypedDict

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.types import interrupt

from shared.examples.graphs.react import build_react_graph
from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_core_tools, get_tool_by_name
from shared.langgraph.checkpointer import get_checkpointer
from shared.utils.llm import get_chat_model


class HITLState(TypedDict):
    messages: Annotated[list, add_messages]
    pending_ticket: dict


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk", sqlite: bool = True):
    s = get_scenario(scenario)
    side_effect_name = s.hitl_side_effect_tool.name
    research_tools = [t for t in get_core_tools(scenario) if t.name != side_effect_name]
    researcher = build_react_graph(provider=provider, tools=research_tools)
    planner = get_chat_model(provider=provider)
    side_effect_tool = get_tool_by_name(scenario, side_effect_name)

    def research(state: HITLState):
        msgs = list(state.get("messages") or [])
        if not msgs or not isinstance(msgs[0], SystemMessage):
            msgs = [SystemMessage(content=s.tier1_prompt)] + msgs
        result = researcher.invoke({"messages": msgs})
        return {"messages": result["messages"]}

    def propose_ticket(state: HITLState):
        if scenario == "ecommerce":
            schema = (
                "Extract refund proposal as JSON with keys: order_id, amount (number), reason."
            )
            default = {"order_id": "48291", "amount": 10.0, "reason": "Shipping delay"}
        elif scenario == "demand-forecast":
            schema = (
                "Extract model registration proposal as JSON with keys: "
                "model_id, stage (staging|production)."
            )
            default = {"model_id": "fcst-3001", "stage": "production"}
        else:
            schema = (
                "Extract ticket proposal as JSON with keys: title, description, priority. "
                "Priority must be low|medium|high."
            )
            default = {
                "title": "Support issue",
                "description": "Escalation needed",
                "priority": "medium",
            }
        r = planner.invoke(
            [
                SystemMessage(content=schema),
                HumanMessage(content=str(state["messages"][-2:])),
            ]
        )
        text = r.content
        proposal = dict(default)
        try:
            proposal = json.loads(text[text.find("{") : text.rfind("}") + 1])
        except (ValueError, json.JSONDecodeError):
            pass
        return {
            "pending_ticket": proposal,
            "messages": [AIMessage(content=f"Proposed action: {proposal}")],
        }

    def human_approval(state: HITLState):
        decision = interrupt(
            {
                "message": f"Approve {side_effect_name}?",
                "ticket": state["pending_ticket"],
                "hint": "Resume with Command(resume='approved') or Command(resume='rejected')",
            }
        )
        if decision != "approved":
            return {"messages": [AIMessage(content=f"{side_effect_name} rejected by human.")]}
        result = side_effect_tool.invoke(state["pending_ticket"])
        return {"messages": [AIMessage(content=result)]}

    graph = StateGraph(HITLState)
    graph.add_node("research", research)
    graph.add_node("propose", propose_ticket)
    graph.add_node("approve", human_approval)
    graph.add_edge(START, "research")
    graph.add_edge("research", "propose")
    graph.add_edge("propose", "approve")
    graph.add_edge("approve", END)
    return graph.compile(checkpointer=get_checkpointer(sqlite=sqlite))
