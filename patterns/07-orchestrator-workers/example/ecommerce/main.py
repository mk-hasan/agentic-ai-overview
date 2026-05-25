"""Run 07-orchestrator-workers — ecommerce scenario."""
from pathlib import Path
from shared.examples.cli import bootstrap_path, run_scenario_entry

bootstrap_path()
run_scenario_entry(Path(__file__).resolve().parent.parent, "ecommerce")
