"""Event-Driven — process inbound support email events."""

import json
from typing import Annotated, TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages

from shared.examples.graphs.react import build_react_graph
from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_core_tools


class EventState(TypedDict):
    event: dict
    user_request: str
    messages: Annotated[list, add_messages]
    response: str


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk"):
    s = get_scenario(scenario)
    agent_subgraph = build_react_graph(provider=provider, tools=get_core_tools(scenario))

    def ingest_event(state: EventState):
        event = state.get("event") or json.loads(s.event_path.read_text(encoding="utf-8"))
        body = (
            f"Support email from {event['from']}\n"
            f"Subject: {event['subject']}\n"
            f"Body: {event['body']}"
        )
        return {"event": event, "user_request": body}

    def prepare_agent(state: EventState):
        return {
            "messages": [
                SystemMessage(content=s.base_system_prompt + s.event_system_suffix),
                HumanMessage(content=state["user_request"]),
            ]
        }

    def finalize_response(state: EventState):
        content = state["messages"][-1].content if state.get("messages") else ""
        return {"response": content}

    handler = StateGraph(EventState)
    handler.add_node("prepare", prepare_agent)
    handler.add_node("agent", agent_subgraph)
    handler.add_node("finalize", finalize_response)
    handler.add_edge(START, "prepare")
    handler.add_edge("prepare", "agent")
    handler.add_edge("agent", "finalize")
    handler.add_edge("finalize", END)
    handler_subgraph = handler.compile()

    graph = StateGraph(EventState)
    graph.add_node("ingest", ingest_event)
    graph.add_node("handle", handler_subgraph)
    graph.add_edge(START, "ingest")
    graph.add_edge("ingest", "handle")
    graph.add_edge("handle", END)
    return graph.compile()
