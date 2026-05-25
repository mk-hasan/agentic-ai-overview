"""Shared pytest fixtures."""

import os

import pytest

from shared.examples.demand_forecast.mlflow_tracking import set_mlflow_enabled
from shared.examples.tool_provider import set_mcp_enabled


@pytest.fixture(autouse=True)
def reset_tool_flags(monkeypatch):
    """Keep tests isolated from host env flags."""
    monkeypatch.delenv("USE_MCP", raising=False)
    monkeypatch.delenv("USE_MLFLOW", raising=False)
    set_mcp_enabled(False)
    set_mlflow_enabled(False)


@pytest.fixture
def helpdesk_scenario():
    from shared.examples.scenarios import get_scenario

    return get_scenario("helpdesk")
