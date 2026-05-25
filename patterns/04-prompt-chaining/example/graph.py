"""Prompt chaining — extract → classify → draft → format."""

from typing import TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph

from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_core_tools, get_extended_tools, get_tool_catalog, get_tools_by_name, get_tool_by_name
from shared.utils.llm import get_chat_model


class ChainState(TypedDict):
    user_request: str
    extracted_issue: str
    category: str
    draft: str
    final_response: str


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk"):
    s = get_scenario(scenario)
    model = get_chat_model(provider=provider)

    def extract_issue(state: ChainState):
        r = model.invoke(
            [
                SystemMessage(content="Extract the core IT issue in one sentence."),
                HumanMessage(content=state["user_request"]),
            ]
        )
        return {"extracted_issue": r.content.strip()}

    def classify(state: ChainState):
        r = model.invoke(
            [
                SystemMessage(content=s.classify_prompt),
                HumanMessage(content=state["extracted_issue"]),
            ]
        )
        return {"category": r.content.strip().lower()}

    def draft_response(state: ChainState):
        r = model.invoke(
            [
                SystemMessage(content=s.base_system_prompt + "\nDraft troubleshooting steps. No ticket yet."),
                HumanMessage(
                    content=f"Issue: {state['extracted_issue']}\nCategory: {state['category']}"
                ),
            ]
        )
        return {"draft": r.content.strip()}

    def format_response(state: ChainState):
        r = model.invoke(
            [
                SystemMessage(content="Format as a friendly helpdesk reply with bullet steps and a short closing."),
                HumanMessage(content=state["draft"]),
            ]
        )
        return {"final_response": r.content.strip()}

    graph = StateGraph(ChainState)
    graph.add_node("extract", extract_issue)
    graph.add_node("classify", classify)
    graph.add_node("draft", draft_response)
    graph.add_node("format", format_response)
    graph.add_edge(START, "extract")
    graph.add_edge("extract", "classify")
    graph.add_edge("classify", "draft")
    graph.add_edge("draft", "format")
    graph.add_edge("format", END)
    return graph.compile()
