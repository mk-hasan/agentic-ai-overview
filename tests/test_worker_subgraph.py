"""Tests for worker ReAct subgraph builder."""

from langchain_core.messages import AIMessage
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool

from shared.examples.graphs.worker_subgraph import build_worker_react_subgraph


@tool
def ping() -> str:
    """Ping tool."""
    return "pong"


class SequenceModel:
    def __init__(self, responses):
        self._responses = list(responses)

    def invoke(self, messages):
        return self._responses.pop(0)


def test_worker_subgraph_runs_tool_loop(monkeypatch):
    tool_call = AIMessage(
        content="",
        tool_calls=[{"name": "ping", "args": {}, "id": "c1", "type": "tool_call"}],
    )
    model = SequenceModel([tool_call, AIMessage(content="done")])

    monkeypatch.setattr(
        "shared.examples.graphs.worker_subgraph.get_chat_model",
        lambda **kwargs: type("M", (), {"bind_tools": lambda self, t: model})(),
    )

    subgraph = build_worker_react_subgraph(
        name="data",
        system_prompt="test worker",
        tools=[ping],
        provider="openai",
    )
    result = subgraph.invoke(
        {"messages": [], "user_request": "load data", "rounds": 0},
    )
    assert result["rounds"] == 1
    assert any("[data worker engaged]" in (getattr(m, "content", "") or "") for m in result["messages"])
