"""Tests for shared.examples.cli flag wiring."""

import argparse

from shared.examples.cli import apply_mcp_cli, apply_mlflow_cli


def test_apply_mlflow_cli_no_flag_enables_by_default(monkeypatch):
    monkeypatch.delenv("USE_MLFLOW", raising=False)
    args = argparse.Namespace(no_mlflow=False)
    apply_mlflow_cli(args)
    import os

    assert os.getenv("USE_MLFLOW") == "1"


def test_apply_mlflow_cli_no_flag_disables(monkeypatch):
    monkeypatch.delenv("USE_MLFLOW", raising=False)
    args = argparse.Namespace(no_mlflow=True)
    apply_mlflow_cli(args)
    import os

    assert os.getenv("USE_MLFLOW") == "0"


def test_apply_mcp_cli_use_mcp(monkeypatch):
    monkeypatch.delenv("USE_MCP", raising=False)
    args = argparse.Namespace(use_mcp=True)
    apply_mcp_cli(args)
    import os

    assert os.getenv("USE_MCP") == "1"


def test_apply_mcp_cli_default_off(monkeypatch):
    monkeypatch.delenv("USE_MCP", raising=False)
    args = argparse.Namespace(use_mcp=False)
    apply_mcp_cli(args)
    import os

    assert os.getenv("USE_MCP") == "0"
