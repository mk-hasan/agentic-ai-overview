"""Mock e-commerce support tools."""

from langchain_core.tools import tool

from shared.examples.ecommerce.constants import DEFAULT_CUSTOMER_EMAIL, DEFAULT_ORDER_ID
from shared.examples.ecommerce.policies import POLICY_ENTRIES
from shared.examples.helpdesk.guardrails import validate_ticket

_ORDERS = {
    "48291": {
        "customer": "jordan.lee@example.com",
        "status": "in_transit",
        "eta": "2026-05-28",
        "address": "123 Home Street, Austin, TX",
        "total": 149.99,
        "items": "Wireless headphones x1",
    },
    "48102": {
        "customer": "sam.park@example.com",
        "status": "delivered",
        "eta": "2026-05-18",
        "address": "88 Lake Ave, Seattle, WA",
        "total": 59.00,
        "items": "USB-C cable x2",
    },
}

_RMA_COUNTER = 5000


def _search_policies_impl(query: str) -> str:
    query_lower = query.lower()
    matches = []
    for key, entry in POLICY_ENTRIES.items():
        haystack = f"{entry['title']} {entry['text']} {' '.join(entry['tags'])}".lower()
        if any(word in haystack for word in query_lower.split() if len(word) > 2):
            matches.append(f"[{key}] {entry['title']}: {entry['text']}")
    if not matches:
        return "No policy entries found. Escalate to Tier-2 if needed."
    return "\n".join(matches)


@tool
def search_policies(query: str) -> str:
    """Search store policies (shipping, returns, orders) for relevant guidance."""
    return _search_policies_impl(query)


@tool
def get_order(order_id: str) -> str:
    """Look up order status, items, ETA, and shipping address by order number."""
    order = _ORDERS.get(order_id.strip().lstrip("#"))
    if not order:
        return f"No order found for ID {order_id}."
    return (
        f"Order #{order_id.lstrip('#')}: {order['status']} | ETA {order['eta']} | "
        f"Items: {order['items']} | Ship to: {order['address']} | Total: ${order['total']}"
    )


@tool
def check_shipping_status(order_id: str = DEFAULT_ORDER_ID) -> str:
    """Check carrier/shipping status for an order."""
    order = _ORDERS.get(order_id.strip().lstrip("#"))
    if not order:
        return f"No shipping data for order {order_id}."
    return (
        f"Shipping for #{order_id.lstrip('#')}: {order['status']} — "
        f"carrier reports on-time for ETA {order['eta']}."
    )


@tool
def update_shipping_address(order_id: str, new_address: str) -> str:
    """Update shipping address if the order has not been delivered."""
    oid = order_id.strip().lstrip("#")
    order = _ORDERS.get(oid)
    if not order:
        return f"Cannot update — order {order_id} not found."
    if order["status"] == "delivered":
        return f"Order #{oid} already delivered — address change not possible."
    order["address"] = new_address
    return f"Address updated for order #{oid} to: {new_address}"


@tool
def create_return(order_id: str, reason: str) -> str:
    """Create a return merchandise authorization (RMA)."""
    global _RMA_COUNTER
    oid = order_id.strip().lstrip("#")
    if oid not in _ORDERS:
        return f"Cannot create return — order {order_id} not found."
    _RMA_COUNTER += 1
    rma = f"RMA-{_RMA_COUNTER}"
    return f"Return created: {rma} for order #{oid}. Reason: {reason}"


@tool
def request_refund(order_id: str, amount: float, reason: str) -> str:
    """Request a refund (may require manager approval in production)."""
    oid = order_id.strip().lstrip("#")
    order = _ORDERS.get(oid)
    if not order:
        return f"Cannot refund — order {order_id} not found."
    ok, msg = validate_ticket(f"Refund #{oid}", f"{reason} amount={amount}")
    if not ok:
        return msg
    return f"Refund of ${amount:.2f} initiated for order #{oid}. Reason: {reason}"


@tool
def lookup_customer(email: str = DEFAULT_CUSTOMER_EMAIL) -> str:
    """Look up customer profile and recent order context."""
    profiles = {
        DEFAULT_CUSTOMER_EMAIL: {
            "name": "Jordan Lee",
            "tier": "Gold",
            "recent_order": DEFAULT_ORDER_ID,
        }
    }
    profile = profiles.get(email.lower())
    if not profile:
        return f"No customer profile for {email}."
    return (
        f"Customer: {profile['name']} | Tier: {profile['tier']} | "
        f"Recent order: #{profile['recent_order']}"
    )


CORE_TOOLS = [
    search_policies,
    get_order,
    check_shipping_status,
    update_shipping_address,
    create_return,
    lookup_customer,
]
EXTENDED_TOOLS = CORE_TOOLS + [request_refund]

TOOL_CATALOG = {
    "search_policies": "Search shipping/returns/order policies",
    "get_order": "Look up order details by ID",
    "check_shipping_status": "Carrier status for an order",
    "update_shipping_address": "Change shipping address (side effect)",
    "create_return": "Open an RMA (side effect)",
    "request_refund": "Initiate refund (side effect, may need approval)",
    "lookup_customer": "Customer profile context",
}


def get_core_tools() -> list:
    return list(CORE_TOOLS)


def get_extended_tools() -> list:
    return list(EXTENDED_TOOLS)


def get_tool_catalog() -> dict:
    return dict(TOOL_CATALOG)


def get_tools_by_name(names: list[str]) -> list:
    by_name = {t.name: t for t in EXTENDED_TOOLS}
    return [by_name[n] for n in names if n in by_name]
