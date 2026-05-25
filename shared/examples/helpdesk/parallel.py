"""Parallel tool invocations for helpdesk scenario."""

from shared.examples.helpdesk.tools import (
    check_email_service_status,
    check_vpn_status,
    search_faq,
)


def run_parallel_checks(user_request: str) -> dict:
    return {
        "faq": search_faq.invoke({"query": user_request}),
        "vpn_status": check_vpn_status.invoke({}),
        "email_status": check_email_service_status.invoke({}),
    }
