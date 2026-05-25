"""Shared CLI and runner for multi-scenario pattern examples."""

import argparse
import os
import runpy
import sys
from pathlib import Path

from shared.config.settings import DEFAULT_SCENARIO, SCENARIOS
from shared.examples.scenarios import get_scenario
from shared.utils.cli import add_provider_argument, resolve_provider
from shared.utils.env import load_env


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def bootstrap_path() -> Path:
    root = repo_root()
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    return root


def add_scenario_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--scenario",
        choices=SCENARIOS,
        default=None,
        help=f"Use case scenario (default: DEFAULT_SCENARIO env or '{DEFAULT_SCENARIO}')",
    )


def add_mlflow_argument(parser: argparse.ArgumentParser) -> None:
    """Add --no-mlflow for demand-forecast examples (MLflow on by default)."""
    parser.add_argument(
        "--no-mlflow",
        action="store_true",
        help="Disable MLflow tracking (demand-forecast scenario; uses in-memory mock)",
    )


def add_mcp_argument(parser: argparse.ArgumentParser) -> None:
    """Add --use-mcp to load tools from the local MCP server instead of in-process tools."""
    parser.add_argument(
        "--use-mcp",
        action="store_true",
        help="Use MCP server tools (stdio) instead of local LangChain tools",
    )


def add_stream_argument(parser: argparse.ArgumentParser) -> None:
    """Add streaming flags for chat and pipeline examples."""
    parser.add_argument(
        "--stream",
        action="store_true",
        help="Stream LLM tokens (helpdesk/ecommerce chat examples)",
    )
    parser.add_argument(
        "--no-stream",
        action="store_true",
        help="Disable token streaming for chat examples",
    )
    parser.add_argument(
        "--stream-events",
        action="store_true",
        help="Stream graph node updates (orchestrator / event-driven examples)",
    )


def chat_stream_enabled(args, scenario: str) -> bool:
    if getattr(args, "no_stream", False):
        return False
    if getattr(args, "stream", False):
        return True
    return scenario in ("helpdesk", "ecommerce")


def apply_mlflow_cli(args) -> None:
    """Set USE_MLFLOW env from CLI before tools run."""
    from shared.examples.demand_forecast.mlflow_tracking import set_mlflow_enabled

    if getattr(args, "no_mlflow", False):
        set_mlflow_enabled(False)
    else:
        load_env()
        if os.getenv("USE_MLFLOW") is None:
            set_mlflow_enabled(True)


def apply_mcp_cli(args) -> None:
    """Set USE_MCP env from CLI before graphs load tools."""
    from shared.examples.tool_provider import set_mcp_enabled

    if getattr(args, "use_mcp", False):
        set_mcp_enabled(True)
    else:
        load_env()
        if os.getenv("USE_MCP") is None:
            set_mcp_enabled(False)


def resolve_scenario(explicit: str = None) -> str:
    load_env()
    if explicit:
        return explicit.lower()
    return os.getenv("DEFAULT_SCENARIO", DEFAULT_SCENARIO).lower()


def build_example_parser(description: str) -> argparse.ArgumentParser:
    scenario = get_scenario(DEFAULT_SCENARIO)
    parser = argparse.ArgumentParser(description=description)
    add_provider_argument(parser)
    add_scenario_argument(parser)
    add_mlflow_argument(parser)
    add_mcp_argument(parser)
    add_stream_argument(parser)
    parser.add_argument(
        "question",
        nargs="*",
        help=f"User message (default from active scenario, e.g. {scenario.default_question[:40]}...)",
    )
    return parser


def parse_example_args(description: str) -> tuple:
    parser = build_example_parser(description)
    args = parser.parse_args()
    apply_mlflow_cli(args)
    apply_mcp_cli(args)
    provider = resolve_provider(args.provider)
    scenario = resolve_scenario(args.scenario)
    sc = get_scenario(scenario)
    question = " ".join(args.question) if args.question else sc.default_question
    return args, provider, scenario, question


def run_scenario_entry(example_dir: Path, scenario: str, extra_argv: list = None) -> None:
    """Run example/main.py with a fixed --scenario (used by helpdesk/ and ecommerce/ subdirs)."""
    bootstrap_path()
    main_path = example_dir / "main.py"
    argv = [str(main_path), "--scenario", scenario] + (extra_argv or sys.argv[1:])
    old_argv = sys.argv
    try:
        sys.argv = argv
        runpy.run_path(str(main_path), run_name="__main__")
    finally:
        sys.argv = old_argv
