"""Shared CLI helpers for pattern examples."""

import argparse
import os
from typing import Optional

from shared.config.settings import DEFAULT_PROVIDER, PROVIDERS
from shared.utils.env import load_env


def add_provider_argument(parser: argparse.ArgumentParser) -> None:
    """Add --provider flag (openai | deepseek) to an example CLI."""
    parser.add_argument(
        "--provider",
        choices=PROVIDERS,
        default=None,
        help=f"LLM provider (default: DEFAULT_PROVIDER env or '{DEFAULT_PROVIDER}')",
    )


def resolve_provider(explicit: Optional[str] = None) -> str:
    """Resolve provider from CLI flag, env, or default."""
    load_env()
    if explicit:
        return explicit.lower()
    return os.getenv("DEFAULT_PROVIDER", DEFAULT_PROVIDER).lower()
