"""LangGraph SQLite checkpointer (durable persistence across runs)."""

from pathlib import Path
from typing import Optional

from shared.config.settings import REPO_ROOT

_holder = {"saver": None, "context": None}


def checkpoint_db_path(explicit: Optional[str] = None) -> Path:
    if explicit:
        return Path(explicit)
    return REPO_ROOT / "data" / "checkpoints" / "langgraph.db"


def get_sqlite_checkpointer(db_path: Optional[str] = None):
    """Return a process-wide SqliteSaver instance."""
    if _holder["saver"] is not None:
        return _holder["saver"]

    try:
        from langgraph.checkpoint.sqlite import SqliteSaver
    except ImportError as exc:
        raise RuntimeError(
            "SQLite checkpointer requires langgraph-checkpoint-sqlite. "
            "Install with: pip install -r requirements-dev.txt"
        ) from exc

    path = checkpoint_db_path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    ctx = SqliteSaver.from_conn_string(str(path))
    _holder["context"] = ctx
    _holder["saver"] = ctx.__enter__()
    return _holder["saver"]


def get_checkpointer(*, sqlite: bool = True, db_path: Optional[str] = None):
    """SQLite by default; in-memory MemorySaver when sqlite=False."""
    if sqlite:
        return get_sqlite_checkpointer(db_path)
    from langgraph.checkpoint.memory import MemorySaver

    return MemorySaver()
