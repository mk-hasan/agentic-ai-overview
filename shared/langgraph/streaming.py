"""Streaming helpers for LangGraph examples."""

import sys
from typing import Any, Dict, Iterable, Optional


def _print_token(token: str) -> None:
    sys.stdout.write(token)
    sys.stdout.flush()


def stream_chat_response(
    graph,
    inputs: dict,
    *,
    config: Optional[dict] = None,
    header: str = "Agent response (streaming)",
) -> dict:
    """
    Stream LLM message tokens (stream_mode='messages') then return final state.
    Falls back to invoke when streaming yields no chunks.
    """
    print(f"\n--- {header} ---\n")
    config = config or {}
    final_state = None
    printed = False

    for chunk in graph.stream(inputs, config=config, stream_mode="messages"):
        if isinstance(chunk, tuple) and len(chunk) == 2:
            message_chunk, _meta = chunk
            text = getattr(message_chunk, "content", "") or ""
            if text:
                _print_token(text)
                printed = True

    if not printed:
        final_state = graph.invoke(inputs, config=config)
        content = final_state["messages"][-1].content
        print(content)
        print()
        return final_state

    print("\n")
    try:
        snap = graph.get_state(config)
        if snap and snap.values:
            return snap.values
    except ValueError:
        pass
    return graph.invoke(inputs, config=config)


def stream_graph_events(
    graph,
    inputs: dict,
    *,
    config: Optional[dict] = None,
    header: str = "Pipeline events",
    interest_keys: Optional[Iterable[str]] = None,
) -> dict:
    """
    Stream node updates (stream_mode='updates') for pipeline progress visibility.
    """
    print(f"\n--- {header} ---")
    keys = set(interest_keys or [])
    final_state = None

    for chunk in graph.stream(inputs, config=config or {}, stream_mode=["updates", "values"]):
        if isinstance(chunk, tuple) and len(chunk) == 2:
            mode, payload = chunk
            if mode == "values":
                final_state = payload
            elif mode == "updates" and isinstance(payload, dict):
                for node, update in payload.items():
                    if keys and node not in keys:
                        continue
                    summary = _summarize_update(update)
                    print(f"  • {node}: {summary}")
        elif isinstance(chunk, dict):
            # stream_mode='updates' only
            for node, update in chunk.items():
                if keys and node not in keys:
                    continue
                summary = _summarize_update(update)
                print(f"  • {node}: {summary}")

    if final_state is not None:
        return final_state
    try:
        snap = graph.get_state(config or {})
        if snap and snap.values:
            return snap.values
    except ValueError:
        pass
    return graph.invoke(inputs, config=config)


def _summarize_update(update: Any) -> str:
    if not isinstance(update, dict):
        return str(update)[:120]
    parts = []
    if "done" in update:
        parts.append(f"done={update['done']}")
    if "next_worker" in update:
        parts.append(f"next={update['next_worker']}")
    if "rounds" in update:
        parts.append(f"rounds={update['rounds']}")
    if "response" in update:
        parts.append(f"response={str(update['response'])[:80]}")
    if "messages" in update and update["messages"]:
        last = update["messages"][-1]
        content = getattr(last, "content", str(last))
        parts.append(f"msg={content[:80]}")
    if "parallel_results" in update:
        parts.append(f"checks={list(update['parallel_results'].keys())}")
    if "event" in update and isinstance(update["event"], dict):
        parts.append(f"event={update['event'].get('subject', 'event')}")
    return ", ".join(parts) if parts else str(update)[:120]
