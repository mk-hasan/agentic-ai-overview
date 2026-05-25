"""Scenario-specific configuration for IT helpdesk graph examples."""

ROUTER_PROMPT = (
    "Route the IT request to exactly one category: vpn, password, email, general."
)
ROUTE_NAMES = ["vpn", "password", "email", "general"]

ORCHESTRATOR_PROMPT = (
    "You are the helpdesk orchestrator. Reply with ONE word: "
    "vpn, password, email, or DONE when the case can close."
)
ORCHESTRATOR_WORKERS = ["vpn", "password", "email"]

CLASSIFY_PROMPT = "Classify the issue as one of: vpn, password, email, hardware, other."

HANDOFF_ESCALATION_PROMPT = (
    "Does this IT case need tier-2 escalation? "
    "Reply YES if recurring VPN drops after FAQ steps, else NO."
)

PARALLEL_TOOL_NAMES = ("search_faq", "check_vpn_status", "check_email_service_status")

RAG_TOOL_NAMES = ["check_vpn_status", "check_email_service_status", "lookup_employee", "create_ticket"]

TIER1_TOOL_NAMES = ["search_faq", "create_ticket"]
TIER2_TOOL_NAMES = ["search_faq", "create_ticket", "collect_vpn_logs"]

WORKER_PROMPTS = {
    "vpn": "VPN_WORKER_PROMPT",
    "password": "PASSWORD_WORKER_PROMPT",
    "email": "EMAIL_WORKER_PROMPT",
}

WORKER_TOOL_NAMES = {
    "vpn": ["search_faq", "create_ticket"],
    "password": ["search_faq", "create_ticket"],
    "email": ["search_faq", "create_ticket"],
}

ROUTE_PROMPT_KEYS = {
    "vpn": "VPN_WORKER_PROMPT",
    "password": "PASSWORD_WORKER_PROMPT",
    "email": "EMAIL_WORKER_PROMPT",
    "general": None,
}

GENERAL_HANDLER_PROMPT = "Handle general IT requests."

REACT_SUFFIX = """
Follow ReAct behavior:
1. Reason about the user's issue.
2. Search the FAQ before escalating.
3. Open a ticket only if FAQ steps are insufficient or the user asks for follow-up."""

EVENT_SYSTEM_SUFFIX = "\nYou are processing an inbound support email event."

MAP_REDUCE_GOAL = (
    "Produce an executive incident report with themes, affected users, and recommended actions."
)
