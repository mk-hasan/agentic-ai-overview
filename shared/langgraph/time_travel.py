"""Time travel helpers — list checkpoints and fork from prior state."""

from typing import Any, Dict, List, Optional


def list_checkpoint_summaries(graph, config: dict, limit: int = 10) -> List[Dict[str, Any]]:
    """Return recent checkpoint summaries newest-first."""
    summaries = []
    for snap in graph.get_state_history(config):
        summaries.append(
            {
                "checkpoint_id": snap.config.get("configurable", {}).get("checkpoint_id"),
                "next": snap.next,
                "message_count": len(snap.values.get("messages") or []),
                "pending_ticket": snap.values.get("pending_ticket"),
                "rounds": snap.values.get("rounds"),
            }
        )
        if len(summaries) >= limit:
            break
    return summaries


def print_checkpoint_history(graph, config: dict, *, title: str = "Checkpoint history") -> None:
    summaries = list_checkpoint_summaries(graph, config)
    print(f"\n--- {title} ({len(summaries)} snapshots) ---")
    for i, item in enumerate(summaries):
        print(
            f"  [{i}] next={item['next']} messages={item['message_count']} "
            f"checkpoint_id={item['checkpoint_id']}"
        )


def fork_from_prior_checkpoint(
    graph,
    config: dict,
    *,
    index: int = 1,
    values: Optional[dict] = None,
) -> dict:
    """
    Fork from a prior checkpoint (index 1 = step before current).
    Returns the new config to pass to subsequent invoke/stream calls.
    """
    history = list(graph.get_state_history(config))
    if len(history) <= index:
        raise ValueError(f"Not enough history to fork at index {index} (have {len(history)})")
    prior = history[index]
    update = values or {}
    new_config = graph.update_state(prior.config, update)
    return new_config


def replay_hitl_with_ticket_patch(
    graph,
    config: dict,
    ticket_patch: dict,
    *,
    history_index: int = 1,
) -> dict:
    """Time-travel demo: rewind and patch pending_ticket before approval resumes."""
    history = list(graph.get_state_history(config))
    if not history:
        raise ValueError("No checkpoint history available")
    target = history[min(history_index, len(history) - 1)]
    prior_ticket = dict(target.values.get("pending_ticket") or {})
    prior_ticket.update(ticket_patch)
    return graph.update_state(target.config, values={"pending_ticket": prior_ticket})
