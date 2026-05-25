"""Parallel tool invocations for e-commerce scenario."""

from shared.examples.ecommerce.constants import DEFAULT_ORDER_ID
from shared.examples.ecommerce.tools import check_shipping_status, get_order, search_policies


def run_parallel_checks(user_request: str) -> dict:
    return {
        "policies": search_policies.invoke({"query": user_request}),
        "order": get_order.invoke({"order_id": DEFAULT_ORDER_ID}),
        "shipping_status": check_shipping_status.invoke({"order_id": DEFAULT_ORDER_ID}),
    }
