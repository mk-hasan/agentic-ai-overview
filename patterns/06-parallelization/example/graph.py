"""Parallelization — fan out checks concurrently, then merge."""

from typing import TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph

from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_core_tools, get_extended_tools, get_tool_catalog, get_tools_by_name, get_tool_by_name
from shared.utils.llm import get_chat_model


class ParallelState(TypedDict):
    user_request: str
    parallel_results: dict
    final_response: str


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk"):
    s = get_scenario(scenario)
    model = get_chat_model(provider=provider)

    def parallel_gather(state: ParallelState):
        results = s.run_parallel_checks(state["user_request"])
        return {"parallel_results": results}

    def synthesize(state: ParallelState):
        context = "\n\n".join(f"{key}:\n{value}" for key, value in state["parallel_results"].items())
        r = model.invoke(
            [
                SystemMessage(content=s.base_system_prompt + "\nSynthesize parallel findings into one reply."),
                HumanMessage(content=f"User issue: {state['user_request']}\n\n{context}"),
            ]
        )
        return {"final_response": r.content.strip()}

    graph = StateGraph(ParallelState)
    graph.add_node("gather", parallel_gather)
    graph.add_node("synthesize", synthesize)
    graph.add_edge(START, "gather")
    graph.add_edge("gather", "synthesize")
    graph.add_edge("synthesize", END)
    return graph.compile()
