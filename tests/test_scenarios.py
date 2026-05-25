"""Tests for scenario registry."""

import pytest

from shared.config.settings import SCENARIOS
from shared.examples.scenarios import get_scenario


def test_all_scenarios_registered():
    for name in SCENARIOS:
        scenario = get_scenario(name)
        assert scenario.name == name


def test_unknown_scenario_raises():
    with pytest.raises(ValueError, match="Unknown scenario"):
        get_scenario("not-a-scenario")


@pytest.mark.parametrize("scenario", SCENARIOS)
def test_parallel_checks_return_expected_keys(scenario):
    sc = get_scenario(scenario)
    results = sc.run_parallel_checks(sc.default_question)
    assert isinstance(results, dict)
    assert len(results) >= 2
    for value in results.values():
        assert isinstance(value, str)
        assert value.strip()


def test_helpdesk_hitl_side_effect_tool_name(helpdesk_scenario):
    assert helpdesk_scenario.hitl_side_effect_tool.name == "create_ticket"
