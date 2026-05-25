"""Scenario-specific configuration for graph examples."""

ROUTER_PROMPT = (
    "Route the customer request to exactly one category: orders, shipping, returns, billing, general."
)
ROUTE_NAMES = ["orders", "shipping", "returns", "billing", "general"]

ORCHESTRATOR_PROMPT = (
    "You are the support orchestrator. Reply with ONE word: "
    "orders, shipping, returns, billing, or DONE when the case can close."
)
ORCHESTRATOR_WORKERS = ["orders", "shipping", "returns", "billing"]

CLASSIFY_PROMPT = "Classify the issue as one of: orders, shipping, returns, billing, other."

HANDOFF_ESCALATION_PROMPT = (
    "Does this case need tier-2 escalation? "
    "Reply YES for refund requests, repeated delivery failures, or policy exceptions, else NO."
)

PARALLEL_TOOL_NAMES = ("search_policies", "get_order", "check_shipping_status")

RAG_TOOL_NAMES = ["update_shipping_address", "create_return", "lookup_customer"]

TIER1_TOOL_NAMES = ["search_policies", "get_order"]
TIER2_TOOL_NAMES = ["search_policies", "get_order", "request_refund", "create_return"]

WORKER_PROMPTS = {
    "orders": "ORDERS_WORKER_PROMPT",
    "shipping": "SHIPPING_WORKER_PROMPT",
    "returns": "RETURNS_WORKER_PROMPT",
    "billing": "BILLING_WORKER_PROMPT",
}

WORKER_TOOL_NAMES = {
    "orders": ["search_policies", "get_order"],
    "shipping": ["search_policies", "get_order", "update_shipping_address"],
    "returns": ["search_policies", "create_return"],
    "billing": ["search_policies", "request_refund"],
}

ROUTE_PROMPT_KEYS = {
    "orders": "ORDERS_WORKER_PROMPT",
    "shipping": "SHIPPING_WORKER_PROMPT",
    "returns": "RETURNS_WORKER_PROMPT",
    "billing": "BILLING_WORKER_PROMPT",
    "general": None,
}

GENERAL_HANDLER_PROMPT = "Handle general e-commerce customer requests."

REACT_SUFFIX = """
Follow ReAct behavior:
1. Understand the customer's order or policy question.
2. Search policies and look up the order before proposing actions.
3. Create returns or request refunds only when policy allows."""

EVENT_SYSTEM_SUFFIX = "\nYou are processing an inbound customer support email about an order."

MAP_REDUCE_GOAL = (
    "Produce an executive support report with recurring themes, affected orders, and recommended actions."
)
