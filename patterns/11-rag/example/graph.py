"""RAG — retrieve from KB markdown, then answer with tools."""

from typing import Annotated, TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_core_tools, get_extended_tools, get_tool_catalog, get_tools_by_name, get_tool_by_name
from shared.utils.llm import get_chat_model


class RAGState(TypedDict):
    messages: Annotated[list, add_messages]
    user_request: str
    context: str


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk"):
    s = get_scenario(scenario)
    rag_tools = get_tools_by_name(scenario, s.rag_tool_names)
    model = get_chat_model(provider=provider).bind_tools(rag_tools)

    def retrieve(state: RAGState):
        chunks = s.retrieve_from_markdown(state["user_request"])
        return {"context": s.format_retrieved_context(chunks)}

    def agent(state: RAGState):
        system = (
            s.base_system_prompt
            + "\n\nRetrieved knowledge base:\n"
            + state["context"]
            + "\n\nDo not use search_faq — rely on retrieved context above."
        )
        response = model.invoke(
            [SystemMessage(content=system), HumanMessage(content=state["user_request"])]
        )
        return {"messages": [response]}

    graph = StateGraph(RAGState)
    graph.add_node("retrieve", retrieve)
    graph.add_node("agent", agent)
    graph.add_node("tools", ToolNode(rag_tools))
    graph.add_edge(START, "retrieve")
    graph.add_edge("retrieve", "agent")
    graph.add_conditional_edges("agent", tools_condition)
    graph.add_edge("tools", "agent")
    return graph.compile()
