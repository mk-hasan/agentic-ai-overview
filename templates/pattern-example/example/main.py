"""Example entry point — use shared provider helpers in every pattern."""

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from shared.utils.cli import add_provider_argument, resolve_provider


def main() -> None:
    parser = argparse.ArgumentParser(description="Pattern example")
    add_provider_argument(parser)
    args = parser.parse_args()

    provider = resolve_provider(args.provider)
    # graph = build_graph(provider=provider)
    print(f"Implement your pattern example here (provider={provider}).")


if __name__ == "__main__":
    main()
