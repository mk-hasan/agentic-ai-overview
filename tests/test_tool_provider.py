"""Tests for shared.examples.tool_provider."""

import pytest

from shared.examples.tool_provider import (
    get_core_tools,
    get_extended_tools,
    get_tool_by_name,
    get_tool_catalog,
    get_tools_by_name,
    is_mcp_enabled,
    set_mcp_enabled,
)


@pytest.mark.parametrize("scenario", ["helpdesk", "ecommerce", "demand-forecast"])
def test_local_core_tools_subset_of_extended(scenario):
    core = {t.name for t in get_core_tools(scenario, use_mcp=False)}
    extended = {t.name for t in get_extended_tools(scenario, use_mcp=False)}
    assert core.issubset(extended)
    assert len(core) > 0


@pytest.mark.parametrize(
    "value,expected",
    [
        ("1", True),
        ("true", True),
        ("on", True),
        ("0", False),
        ("false", False),
        ("", False),
    ],
)
def test_mcp_flag_parsing(value, expected, monkeypatch):
    monkeypatch.setenv("USE_MCP", value)
    assert is_mcp_enabled() is expected


def test_set_mcp_enabled():
    set_mcp_enabled(True)
    assert is_mcp_enabled() is True
    set_mcp_enabled(False)
    assert is_mcp_enabled() is False


def test_get_tools_by_name_preserves_order(helpdesk_scenario):
    names = ["search_faq", "create_ticket", "check_vpn_status"]
    tools = get_tools_by_name("helpdesk", names, use_mcp=False)
    assert [t.name for t in tools] == names


def test_get_tool_by_name_missing_raises():
    with pytest.raises(KeyError):
        get_tool_by_name("helpdesk", "not_a_real_tool", use_mcp=False)


def test_tool_catalog_matches_extended_tools():
    catalog = get_tool_catalog("helpdesk", use_mcp=False)
    names = {t.name for t in get_extended_tools("helpdesk", use_mcp=False)}
    assert set(catalog) == names


def test_mcp_mode_raises_on_python_39():
    set_mcp_enabled(True)
    with pytest.raises(RuntimeError, match="Python 3.10"):
        get_core_tools("helpdesk")
