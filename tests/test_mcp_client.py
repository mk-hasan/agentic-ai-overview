"""Tests for MCP client helpers."""

from shared.mcp.client import mcp_server_script


def test_mcp_server_script_points_to_repo_file():
    path = mcp_server_script()
    assert path.endswith("shared/mcp/server.py")
