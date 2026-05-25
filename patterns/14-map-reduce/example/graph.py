"""Map–Reduce — summarize many incident logs into an executive report."""

import json
from typing import List, TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph

from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_core_tools, get_extended_tools, get_tool_catalog, get_tools_by_name, get_tool_by_name
from shared.utils.llm import get_chat_model


class MapReduceState(TypedDict):
    incidents: List[dict]
    partial_summaries: List[str]
    final_report: str


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk"):
    s = get_scenario(scenario)
    model = get_chat_model(provider=provider)

    def load_incidents(state: MapReduceState):
        incidents = json.loads(s.incidents_path.read_text(encoding="utf-8"))
        return {"incidents": incidents, "partial_summaries": []}

    def map_summaries(state: MapReduceState):
        partials = []
        for item in state["incidents"]:
            r = model.invoke(
                [
                    SystemMessage(content="Summarize this incident log in 2 sentences."),
                    HumanMessage(content=json.dumps(item)),
                ]
            )
            partials.append(f"{item['id']}: {r.content.strip()}")
        return {"partial_summaries": partials}

    def reduce_report(state: MapReduceState):
        joined = "\n".join(state["partial_summaries"])
        r = model.invoke(
            [
                SystemMessage(content=s.base_system_prompt + "\n" + s.map_reduce_goal),
                HumanMessage(content=joined),
            ]
        )
        return {"final_report": r.content.strip()}

    graph = StateGraph(MapReduceState)
    graph.add_node("load", load_incidents)
    graph.add_node("map", map_summaries)
    graph.add_node("reduce", reduce_report)
    graph.add_edge(START, "load")
    graph.add_edge("load", "map")
    graph.add_edge("map", "reduce")
    graph.add_edge("reduce", END)
    return graph.compile()
