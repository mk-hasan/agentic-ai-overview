"""Tests for orchestrator helper functions."""

import pytest
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode

from shared.examples.orchestrator_utils import (
    max_orchestrator_rounds,
    parse_orchestrator_choice,
    run_worker_tool_loop,
)


WORKERS = ["data", "features", "modeling", "deployment", "monitoring"]


@pytest.mark.parametrize(
    "content,expected_worker,expected_done",
    [
        ("DONE", "data", True),
        ("done.", "data", True),
        ("modeling", "modeling", False),
        ("Next: features please", "features", False),
        ("", "data", False),
        ("unknown step", "data", False),
    ],
)
def test_parse_orchestrator_choice(content, expected_worker, expected_done):
    worker, done = parse_orchestrator_choice(content, WORKERS, "data")
    assert worker == expected_worker
    assert done is expected_done


def test_parse_orchestrator_choice_avoids_substring_false_positive():
    worker, done = parse_orchestrator_choice("metadata issue", WORKERS, "data")
    assert worker == "data"
    assert done is False


def test_max_orchestrator_rounds():
    assert max_orchestrator_rounds(5) == 7
    assert max_orchestrator_rounds(3) == 5


@tool
def echo(value: str) -> str:
    """Echo a value."""
    return f"echo:{value}"


class SequenceModel:
    def __init__(self, responses):
        self._responses = list(responses)
        self.calls = 0

    def invoke(self, messages):
        self.calls += 1
        return self._responses.pop(0)


def test_run_worker_tool_loop_single_turn():
    model = SequenceModel([AIMessage(content="finished")])
    messages = run_worker_tool_loop([HumanMessage(content="hi")], model, ToolNode([echo]))
    assert len(messages) == 1
    assert messages[0].content == "finished"
    assert model.calls == 1


def test_run_worker_tool_loop_executes_tools_then_follows_up():
    tool_call = AIMessage(
        content="",
        tool_calls=[
            {
                "name": "echo",
                "args": {"value": "ping"},
                "id": "call-1",
                "type": "tool_call",
            }
        ],
    )
    model = SequenceModel([tool_call, AIMessage(content="done after tool")])
    messages = run_worker_tool_loop([HumanMessage(content="hi")], model, ToolNode([echo]))

    assert len(messages) == 3
    assert messages[0].tool_calls
    assert isinstance(messages[1], ToolMessage)
    assert messages[1].content == "echo:ping"
    assert messages[2].content == "done after tool"
    assert model.calls == 2
