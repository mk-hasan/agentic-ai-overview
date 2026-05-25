"""LangGraph worker ReAct subgraph for orchestrator–workers pattern."""

from typing import Annotated, TypedDict

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from shared.utils.llm import get_chat_model


class WorkerSubgraphState(TypedDict):
    """Shared with parent orchestrator state keys."""

    messages: Annotated[list, add_messages]
    user_request: str
    rounds: int


def build_worker_react_subgraph(
    *,
    name: str,
    system_prompt: str,
    tools: list,
    provider: str,
):
    """Compile a ReAct tool loop as a LangGraph subgraph node."""
    model = get_chat_model(provider=provider).bind_tools(tools)

    def prepare(state: WorkerSubgraphState):
        engaged = AIMessage(content=f"[{name} worker engaged]")
        msgs = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=state["user_request"]),
        ] + list(state.get("messages") or [])
        return {"messages": [engaged] + msgs}

    def call_model(state: WorkerSubgraphState):
        return {"messages": [model.invoke(state["messages"])]}

    def finalize(state: WorkerSubgraphState):
        return {"rounds": state.get("rounds", 0) + 1}

    def route_after_agent(state: WorkerSubgraphState):
        last = state["messages"][-1]
        if getattr(last, "tool_calls", None):
            return "tools"
        return "finalize"

    graph = StateGraph(WorkerSubgraphState)
    graph.add_node("prepare", prepare)
    graph.add_node("agent", call_model)
    graph.add_node("tools", ToolNode(tools))
    graph.add_node("finalize", finalize)
    graph.add_edge(START, "prepare")
    graph.add_edge("prepare", "agent")
    graph.add_conditional_edges(
        "agent",
        route_after_agent,
        {"tools": "tools", "finalize": "finalize"},
    )
    graph.add_edge("tools", "agent")
    graph.add_edge("finalize", END)
    return graph.compile()
