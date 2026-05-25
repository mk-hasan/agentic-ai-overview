"""Routing — classify intent and dispatch to specialist handlers."""

from typing import TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph

from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_core_tools, get_extended_tools, get_tool_catalog, get_tools_by_name, get_tool_by_name
from shared.utils.llm import get_chat_model


class RouteState(TypedDict):
    user_request: str
    route: str
    response: str


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk"):
    s = get_scenario(scenario)
    model = get_chat_model(provider=provider)

    def router(state: RouteState):
        r = model.invoke(
            [
                SystemMessage(content=s.router_prompt),
                HumanMessage(content=state["user_request"]),
            ]
        )
        route = r.content.strip().lower()
        for key in s.route_names:
            if key != "general" and key in route:
                return {"route": key}
        return {"route": "general"}

    def handler(system_extra: str):
        def node(state: RouteState):
            r = model.invoke(
                [
                    SystemMessage(content=s.base_system_prompt + "\n" + system_extra),
                    HumanMessage(content=state["user_request"]),
                ]
            )
            return {"response": r.content.strip()}

        return node

    graph = StateGraph(RouteState)
    graph.add_node("router", router)
    for route in s.route_names:
        graph.add_node(route, handler(s.get_route_prompt(route)))
    graph.add_edge(START, "router")
    graph.add_conditional_edges(
        "router",
        lambda st: st["route"],
        {route: route for route in s.route_names},
    )
    for route in s.route_names:
        graph.add_edge(route, END)
    return graph.compile()
