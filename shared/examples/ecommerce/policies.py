"""Policy entries for e-commerce support tools and RAG."""

POLICY_ENTRIES = {
    "shipping": {
        "title": "Shipping and delivery",
        "text": (
            "Standard shipping is 3–5 business days. Express is 1–2 days. "
            "Address changes are allowed before the package ships or while in transit "
            "with carrier approval."
        ),
        "tags": ["shipping", "delivery", "address", "tracking"],
    },
    "returns": {
        "title": "Returns within 30 days",
        "text": (
            "Items may be returned within 30 days in original condition. "
            "Open an RMA before sending items back. Refunds process in 5–7 business days."
        ),
        "tags": ["return", "refund", "rma", "exchange"],
    },
    "orders": {
        "title": "Order tracking",
        "text": (
            "Use your order number to check status: processing, shipped, in_transit, delivered. "
            "Contact support if tracking has not updated in 48 hours."
        ),
        "tags": ["order", "tracking", "status", "eta"],
    },
}
