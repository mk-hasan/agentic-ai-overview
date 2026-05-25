"""Backward-compatible CLI — prefer shared.examples.cli."""

from shared.examples.cli import (  # noqa: F401
    bootstrap_path,
    build_example_parser,
    parse_example_args,
    resolve_scenario,
    run_scenario_entry,
)


def parse_helpdesk_args(description: str):
    args, provider, scenario, question = parse_example_args(description)
    return args, provider, question


def build_helpdesk_parser(description: str):
    return build_example_parser(description)
