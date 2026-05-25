"""Unified scenario registry for pattern examples."""

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional

from shared.config.settings import REPO_ROOT, SCENARIOS, DEFAULT_SCENARIO


@dataclass
class Scenario:
    name: str
    display_name: str
    default_question: str
    follow_up_question: str
    base_system_prompt: str
    tier1_prompt: str
    tier2_prompt: str
    react_suffix: str
    router_prompt: str
    route_names: list
    route_prompt_keys: dict
    general_handler_prompt: str
    orchestrator_prompt: str
    orchestrator_workers: list
    worker_prompts: dict
    worker_tool_names: dict
    classify_prompt: str
    handoff_escalation_prompt: str
    parallel_tool_names: tuple
    rag_tool_names: list
    tier1_tool_names: list
    tier2_tool_names: list
    event_system_suffix: str
    map_reduce_goal: str
    incidents_path: Path
    event_path: Path
    get_core_tools: Callable
    get_extended_tools: Callable
    get_tool_catalog: Callable
    get_tools_by_name: Callable
    retrieve_from_markdown: Callable
    format_retrieved_context: Callable
    prompts_module: object
    run_parallel_checks: Callable
    hitl_side_effect_tool: object
    plan_fallback_steps: list
    mldlc_steps: list

    def get_prompt(self, key: str) -> str:
        return getattr(self.prompts_module, key)

    def get_worker_prompt(self, worker: str) -> str:
        prompt_key = self.worker_prompts[worker]
        return getattr(self.prompts_module, prompt_key)

    def get_route_prompt(self, route: str) -> str:
        key = self.route_prompt_keys.get(route)
        if key:
            return getattr(self.prompts_module, key)
        return self.general_handler_prompt


def _load_helpdesk() -> Scenario:
    from shared.examples.helpdesk import config as cfg
    from shared.examples.helpdesk import constants, parallel, prompts, retrieval, tools

    return Scenario(
        name="helpdesk",
        display_name=constants.SCENARIO_NAME,
        default_question=constants.DEFAULT_QUESTION,
        follow_up_question=constants.FOLLOW_UP_QUESTION,
        base_system_prompt=prompts.BASE_SYSTEM_PROMPT,
        tier1_prompt=prompts.TIER1_PROMPT,
        tier2_prompt=prompts.TIER2_PROMPT,
        react_suffix=cfg.REACT_SUFFIX,
        router_prompt=cfg.ROUTER_PROMPT,
        route_names=cfg.ROUTE_NAMES,
        route_prompt_keys=cfg.ROUTE_PROMPT_KEYS,
        general_handler_prompt=cfg.GENERAL_HANDLER_PROMPT,
        orchestrator_prompt=cfg.ORCHESTRATOR_PROMPT,
        orchestrator_workers=cfg.ORCHESTRATOR_WORKERS,
        worker_prompts=cfg.WORKER_PROMPTS,
        worker_tool_names=cfg.WORKER_TOOL_NAMES,
        classify_prompt=cfg.CLASSIFY_PROMPT,
        handoff_escalation_prompt=cfg.HANDOFF_ESCALATION_PROMPT,
        parallel_tool_names=cfg.PARALLEL_TOOL_NAMES,
        rag_tool_names=cfg.RAG_TOOL_NAMES,
        tier1_tool_names=cfg.TIER1_TOOL_NAMES,
        tier2_tool_names=cfg.TIER2_TOOL_NAMES,
        event_system_suffix=cfg.EVENT_SYSTEM_SUFFIX,
        map_reduce_goal=cfg.MAP_REDUCE_GOAL,
        incidents_path=REPO_ROOT / "shared/examples/helpdesk/data/incidents.json",
        event_path=REPO_ROOT / "shared/examples/helpdesk/data/sample_event.json",
        get_core_tools=tools.get_core_tools,
        get_extended_tools=tools.get_extended_tools,
        get_tool_catalog=tools.get_tool_catalog,
        get_tools_by_name=tools.get_tools_by_name,
        retrieve_from_markdown=retrieval.retrieve_from_markdown,
        format_retrieved_context=retrieval.format_retrieved_context,
        prompts_module=prompts,
        run_parallel_checks=parallel.run_parallel_checks,
        hitl_side_effect_tool=tools.create_ticket,
        plan_fallback_steps=[
            "Search FAQ",
            "Check VPN/status",
            "Respond or open ticket",
        ],
        mldlc_steps=[],
    )


def _load_ecommerce() -> Scenario:
    from shared.examples.ecommerce import config as cfg
    from shared.examples.ecommerce import constants, parallel, prompts, retrieval, tools

    return Scenario(
        name="ecommerce",
        display_name=constants.SCENARIO_NAME,
        default_question=constants.DEFAULT_QUESTION,
        follow_up_question=constants.FOLLOW_UP_QUESTION,
        base_system_prompt=prompts.BASE_SYSTEM_PROMPT,
        tier1_prompt=prompts.TIER1_PROMPT,
        tier2_prompt=prompts.TIER2_PROMPT,
        react_suffix=cfg.REACT_SUFFIX,
        router_prompt=cfg.ROUTER_PROMPT,
        route_names=cfg.ROUTE_NAMES,
        route_prompt_keys=cfg.ROUTE_PROMPT_KEYS,
        general_handler_prompt=cfg.GENERAL_HANDLER_PROMPT,
        orchestrator_prompt=cfg.ORCHESTRATOR_PROMPT,
        orchestrator_workers=cfg.ORCHESTRATOR_WORKERS,
        worker_prompts=cfg.WORKER_PROMPTS,
        worker_tool_names=cfg.WORKER_TOOL_NAMES,
        classify_prompt=cfg.CLASSIFY_PROMPT,
        handoff_escalation_prompt=cfg.HANDOFF_ESCALATION_PROMPT,
        parallel_tool_names=cfg.PARALLEL_TOOL_NAMES,
        rag_tool_names=cfg.RAG_TOOL_NAMES,
        tier1_tool_names=cfg.TIER1_TOOL_NAMES,
        tier2_tool_names=cfg.TIER2_TOOL_NAMES,
        event_system_suffix=cfg.EVENT_SYSTEM_SUFFIX,
        map_reduce_goal=cfg.MAP_REDUCE_GOAL,
        incidents_path=REPO_ROOT / "shared/examples/ecommerce/data/incidents.json",
        event_path=REPO_ROOT / "shared/examples/ecommerce/data/sample_event.json",
        get_core_tools=tools.get_core_tools,
        get_extended_tools=tools.get_extended_tools,
        get_tool_catalog=tools.get_tool_catalog,
        get_tools_by_name=tools.get_tools_by_name,
        retrieve_from_markdown=retrieval.retrieve_from_markdown,
        format_retrieved_context=retrieval.format_retrieved_context,
        prompts_module=prompts,
        run_parallel_checks=parallel.run_parallel_checks,
        hitl_side_effect_tool=tools.request_refund,
        plan_fallback_steps=[
            "Look up order",
            "Check policies and shipping",
            "Respond or escalate",
        ],
        mldlc_steps=[],
    )


def _load_demand_forecast() -> Scenario:
    from shared.examples.demand_forecast import config as cfg
    from shared.examples.demand_forecast import constants, parallel, prompts, retrieval, tools

    return Scenario(
        name="demand-forecast",
        display_name=constants.SCENARIO_NAME,
        default_question=constants.DEFAULT_QUESTION,
        follow_up_question=constants.FOLLOW_UP_QUESTION,
        base_system_prompt=prompts.BASE_SYSTEM_PROMPT,
        tier1_prompt=prompts.TIER1_PROMPT,
        tier2_prompt=prompts.TIER2_PROMPT,
        react_suffix=cfg.REACT_SUFFIX,
        router_prompt=cfg.ROUTER_PROMPT,
        route_names=cfg.ROUTE_NAMES,
        route_prompt_keys=cfg.ROUTE_PROMPT_KEYS,
        general_handler_prompt=cfg.GENERAL_HANDLER_PROMPT,
        orchestrator_prompt=cfg.ORCHESTRATOR_PROMPT,
        orchestrator_workers=cfg.ORCHESTRATOR_WORKERS,
        worker_prompts=cfg.WORKER_PROMPTS,
        worker_tool_names=cfg.WORKER_TOOL_NAMES,
        classify_prompt=cfg.CLASSIFY_PROMPT,
        handoff_escalation_prompt=cfg.HANDOFF_ESCALATION_PROMPT,
        parallel_tool_names=cfg.PARALLEL_TOOL_NAMES,
        rag_tool_names=cfg.RAG_TOOL_NAMES,
        tier1_tool_names=cfg.TIER1_TOOL_NAMES,
        tier2_tool_names=cfg.TIER2_TOOL_NAMES,
        event_system_suffix=cfg.EVENT_SYSTEM_SUFFIX,
        map_reduce_goal=cfg.MAP_REDUCE_GOAL,
        incidents_path=REPO_ROOT / "shared/examples/demand_forecast/data/pipeline_runs.json",
        event_path=REPO_ROOT / "shared/examples/demand_forecast/data/retrain_event.json",
        get_core_tools=tools.get_core_tools,
        get_extended_tools=tools.get_extended_tools,
        get_tool_catalog=tools.get_tool_catalog,
        get_tools_by_name=tools.get_tools_by_name,
        retrieve_from_markdown=retrieval.retrieve_from_markdown,
        format_retrieved_context=retrieval.format_retrieved_context,
        prompts_module=prompts,
        run_parallel_checks=parallel.run_parallel_checks,
        hitl_side_effect_tool=tools.register_model,
        plan_fallback_steps=constants.PLAN_FALLBACK_STEPS,
        mldlc_steps=constants.MLDLC_STEPS,
    )


_LOADERS = {
    "helpdesk": _load_helpdesk,
    "ecommerce": _load_ecommerce,
    "demand-forecast": _load_demand_forecast,
}


def get_scenario(name: Optional[str] = None) -> Scenario:
    selected = (name or DEFAULT_SCENARIO).lower()
    if selected not in SCENARIOS:
        raise ValueError(f"Unknown scenario {selected!r}. Choose from: {', '.join(SCENARIOS)}")
    return _LOADERS[selected]()
