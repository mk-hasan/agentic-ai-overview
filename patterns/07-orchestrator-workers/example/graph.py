"""Orchestrator–Workers — supervisor delegates to specialist worker subgraphs."""

from typing import Annotated, TypedDict

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages

from shared.examples.graphs.worker_subgraph import build_worker_react_subgraph
from shared.examples.orchestrator_utils import max_orchestrator_rounds, parse_orchestrator_choice
from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_tools_by_name
from shared.utils.llm import get_chat_model


class OrchestratorState(TypedDict):
    messages: Annotated[list, add_messages]
    user_request: str
    next_worker: str
    done: bool
    rounds: int


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk"):
    s = get_scenario(scenario)
    workers = {
        name: {
            "prompt": s.get_worker_prompt(name),
            "tools": get_tools_by_name(scenario, s.worker_tool_names[name]),
        }
        for name in s.orchestrator_workers
    }

    orchestrator = get_chat_model(provider=provider)

    worker_subgraphs = {
        name: build_worker_react_subgraph(
            name=name,
            system_prompt=s.base_system_prompt + "\n" + cfg["prompt"],
            tools=cfg["tools"],
            provider=provider,
        )
        for name, cfg in workers.items()
    }

    def supervisor(state: OrchestratorState):
        if state.get("done"):
            return {}
        rounds = state.get("rounds", 0)
        max_rounds = max_orchestrator_rounds(len(workers))
        if rounds >= max_rounds:
            return {
                "done": True,
                "messages": [AIMessage(content="Orchestrator: pipeline steps complete, case closed.")],
            }
        r = orchestrator.invoke(
            [
                SystemMessage(content=s.orchestrator_prompt),
                HumanMessage(
                    content=(
                        f"Request: {state['user_request']}\n"
                        f"Rounds completed: {rounds}/{max_rounds}\n"
                        f"Transcript: {state['messages'][-6:]}"
                    )
                ),
            ]
        )
        next_worker, is_done = parse_orchestrator_choice(
            r.content, list(workers.keys()), s.orchestrator_workers[0]
        )
        if is_done:
            return {"done": True, "messages": [AIMessage(content="Orchestrator: case closed.")]}
        return {"next_worker": next_worker, "done": False}

    graph = StateGraph(OrchestratorState)
    graph.add_node("supervisor", supervisor)
    for name, subgraph in worker_subgraphs.items():
        graph.add_node(name, subgraph)
    graph.add_edge(START, "supervisor")
    graph.add_conditional_edges(
        "supervisor",
        lambda st: END if st.get("done") else st.get("next_worker", s.orchestrator_workers[0]),
        {**{name: name for name in workers}, END: END},
    )
    for name in workers:
        graph.add_edge(name, "supervisor")
    return graph.compile()
