"""Standard ReAct graph builder (scenario-agnostic)."""

from typing import List, Optional

from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from shared.utils.llm import get_chat_model


def build_react_graph(
    *,
    provider: str,
    tools: list,
    checkpointer=None,
    interrupt_before: Optional[List[str]] = None,
):
    model = get_chat_model(provider=provider).bind_tools(tools)

    def call_model(state: MessagesState):
        response = model.invoke(state["messages"])
        return {"messages": [response]}

    graph = StateGraph(MessagesState)
    graph.add_node("agent", call_model)
    graph.add_node("tools", ToolNode(tools))
    graph.add_edge(START, "agent")
    graph.add_conditional_edges("agent", tools_condition)
    graph.add_edge("tools", "agent")

    compile_kwargs = {}
    if checkpointer is not None:
        compile_kwargs["checkpointer"] = checkpointer
    if interrupt_before:
        compile_kwargs["interrupt_before"] = interrupt_before
    return graph.compile(**compile_kwargs)
