"""Graph and routing configuration for demand forecast scenario."""

ROUTER_PROMPT = (
    "Route the ML pipeline request to exactly one category: "
    "data, features, modeling, deployment, monitoring, general."
)
ROUTE_NAMES = ["data", "features", "modeling", "deployment", "monitoring", "general"]

ORCHESTRATOR_PROMPT = (
    "You are the ML pipeline orchestrator. Reply with ONE word: "
    "data, features, modeling, deployment, monitoring, or DONE when finished."
)
ORCHESTRATOR_WORKERS = ["data", "features", "modeling", "deployment", "monitoring"]

CLASSIFY_PROMPT = (
    "Classify the ML request as one of: data, features, modeling, deployment, monitoring, other."
)

HANDOFF_ESCALATION_PROMPT = (
    "Does this ML case need tier-2 escalation? "
    "Reply YES for production deployment, drift response, or retrain promotion, else NO."
)

PARALLEL_TOOL_NAMES = ("load_demand_data", "run_eda", "check_data_drift")

RAG_TOOL_NAMES = ["generate_forecast", "evaluate_model"]

TIER1_TOOL_NAMES = ["search_playbook", "load_demand_data", "run_eda", "train_forecast_model", "evaluate_model"]
TIER2_TOOL_NAMES = [
    "search_playbook",
    "train_forecast_model",
    "evaluate_model",
    "register_model",
    "check_data_drift",
]

WORKER_PROMPTS = {
    "data": "DATA_WORKER_PROMPT",
    "features": "FEATURES_WORKER_PROMPT",
    "modeling": "MODELING_WORKER_PROMPT",
    "deployment": "DEPLOYMENT_WORKER_PROMPT",
    "monitoring": "MONITORING_WORKER_PROMPT",
}

WORKER_TOOL_NAMES = {
    "data": ["search_playbook", "load_demand_data", "run_eda"],
    "features": ["search_playbook", "prepare_features"],
    "modeling": ["search_playbook", "train_forecast_model", "evaluate_model"],
    "deployment": ["search_playbook", "register_model"],
    "monitoring": ["search_playbook", "check_data_drift", "generate_forecast"],
}

ROUTE_PROMPT_KEYS = {
    "data": "DATA_WORKER_PROMPT",
    "features": "FEATURES_WORKER_PROMPT",
    "modeling": "MODELING_WORKER_PROMPT",
    "deployment": "DEPLOYMENT_WORKER_PROMPT",
    "monitoring": "MONITORING_WORKER_PROMPT",
    "general": None,
}

GENERAL_HANDLER_PROMPT = "Handle general ML pipeline planning questions."

REACT_SUFFIX = """
Follow ReAct behavior:
1. Clarify SKU, store, and forecast horizon if missing.
2. Progress through MLDLC steps using tools (data → EDA → train → evaluate).
3. Register to production only after evaluation passes thresholds."""

EVENT_SYSTEM_SUFFIX = "\nYou are processing a scheduled retrain / drift event for the forecast pipeline."

MAP_REDUCE_GOAL = (
    "Produce an ML pipeline summary report: runs by step, SKUs needing attention, and retrain recommendations."
)

PROMPT_CHAIN_STAGES = [
    "extract_scope",
    "classify_mldlc_phase",
    "draft_plan",
    "format_recommendation",
]
