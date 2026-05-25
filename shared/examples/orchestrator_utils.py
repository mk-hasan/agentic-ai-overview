"""Helpers for orchestrator–workers pattern graphs."""

from langchain_core.messages import AIMessage
from langgraph.prebuilt import ToolNode


def parse_orchestrator_choice(content: str, worker_names: list, default: str) -> tuple:
    """Return (next_worker, is_done) from orchestrator LLM output."""
    text = (content or "").strip().lower()
    if not text:
        return default, False
    first = text.split()[0].strip(".,!:")
    if first == "done" or text.startswith("done"):
        return default, True
    for name in worker_names:
        if first == name:
            return name, False
    for name in worker_names:
        if name in text.split():
            return name, False
    return default, False


def run_worker_tool_loop(base_messages: list, model, tool_node: ToolNode, max_steps: int = 6) -> list:
    """Run agent↔tools until the model stops requesting tools."""
    messages = list(base_messages)
    new_messages = []
    for _ in range(max_steps):
        response = model.invoke(messages)
        new_messages.append(response)
        messages.append(response)
        if not getattr(response, "tool_calls", None):
            break
        tool_update = tool_node.invoke({"messages": messages})
        tool_messages = tool_update["messages"]
        new_messages.extend(tool_messages)
        messages.extend(tool_messages)
    return new_messages


def max_orchestrator_rounds(worker_count: int) -> int:
    """Upper bound on supervisor→worker cycles before forced stop."""
    return worker_count + 2
