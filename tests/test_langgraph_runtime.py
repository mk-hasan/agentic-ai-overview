"""Tests for LangGraph runtime helpers."""

import pytest

from shared.examples.orchestrator_utils import parse_orchestrator_choice
from shared.langgraph.time_travel import list_checkpoint_summaries


def test_list_checkpoint_summaries_empty_graph():
    from langchain_core.messages import AIMessage
    from langgraph.checkpoint.memory import MemorySaver
    from langgraph.graph import END, START, StateGraph
    from typing import Annotated, TypedDict
    from langgraph.graph.message import add_messages

    class S(TypedDict):
        messages: Annotated[list, add_messages]
        pending_ticket: dict

    g = StateGraph(S)
    g.add_node("a", lambda s: {"messages": [AIMessage(content="hi")], "pending_ticket": {"x": 1}})
    g.add_edge(START, "a")
    g.add_edge("a", END)
    graph = g.compile(checkpointer=MemorySaver())
    config = {"configurable": {"thread_id": "test-history"}}
    graph.invoke({"messages": [], "pending_ticket": {}}, config=config)
    summaries = list_checkpoint_summaries(graph, config)
    assert len(summaries) >= 1
    assert summaries[0]["message_count"] >= 1


@pytest.mark.parametrize(
    "content,worker,done",
    [
        ("DONE", "data", True),
        ("modeling", "modeling", False),
    ],
)
def test_parse_orchestrator_choice_shared(content, worker, done):
    picked, is_done = parse_orchestrator_choice(content, ["data", "modeling"], "data")
    assert picked == worker
    assert is_done is done


def test_sqlite_checkpointer_requires_package(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "shared.langgraph.checkpointer._holder",
        {"saver": None, "context": None},
    )
    from shared.langgraph import checkpointer as cp

    saver = cp.get_checkpointer(sqlite=True, db_path=str(tmp_path / "test.db"))
    assert saver is not None
