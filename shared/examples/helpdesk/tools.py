"""Mock IT helpdesk tools shared across pattern examples."""

from langchain_core.tools import tool

from shared.examples.helpdesk.constants import DEFAULT_USER_EMAIL
from shared.examples.helpdesk.faq import FAQ_ENTRIES
from shared.examples.helpdesk.guardrails import validate_ticket

_TICKET_COUNTER = 1042
_SYSTEM_STATUS = {
    "vpn": "degraded — elevated disconnect rate in US-East",
    "email": "operational",
    "sso": "operational",
}


def _search_faq_impl(query: str) -> str:
    query_lower = query.lower()
    matches = []
    for key, entry in FAQ_ENTRIES.items():
        haystack = f"{entry['title']} {entry['text']} {' '.join(entry['tags'])}".lower()
        if any(word in haystack for word in query_lower.split() if len(word) > 2):
            matches.append(f"[{key}] {entry['title']}: {entry['text']}")
    if not matches:
        return "No FAQ entries found. Consider opening a ticket for tier-2 support."
    return "\n".join(matches)


@tool
def search_faq(query: str) -> str:
    """Search the internal IT FAQ for troubleshooting steps matching the user's issue."""
    return _search_faq_impl(query)


@tool
def create_ticket(title: str, description: str, priority: str = "medium") -> str:
    """Open an IT support ticket. Use after checking the FAQ or when human follow-up is needed."""
    global _TICKET_COUNTER
    ok, message = validate_ticket(title, description)
    if not ok:
        return message
    _TICKET_COUNTER += 1
    ticket_id = f"INC-{_TICKET_COUNTER}"
    return (
        f"Ticket created: {ticket_id}\n"
        f"Title: {title}\n"
        f"Priority: {priority}\n"
        f"Description: {description}"
    )


@tool
def check_vpn_status(user_email: str = DEFAULT_USER_EMAIL) -> str:
    """Check VPN service health and whether the user site has known issues."""
    return (
        f"VPN status: {_SYSTEM_STATUS['vpn']}. "
        f"No active user-specific outage for {user_email}."
    )


@tool
def check_email_service_status() -> str:
    """Check whether the corporate email service is operational."""
    return f"Email service status: {_SYSTEM_STATUS['email']}."


@tool
def lookup_employee(email: str) -> str:
    """Look up basic employee profile details for support context."""
    profiles = {
        DEFAULT_USER_EMAIL: {
            "name": "Alex Jordan",
            "department": "Engineering",
            "office": "NYC",
            "device": "MacBook Pro",
        }
    }
    profile = profiles.get(email.lower())
    if not profile:
        return f"No employee record found for {email}."
    return (
        f"Employee: {profile['name']} | Dept: {profile['department']} | "
        f"Office: {profile['office']} | Device: {profile['device']}"
    )


@tool
def collect_vpn_logs(user_email: str = DEFAULT_USER_EMAIL) -> str:
    """Request VPN client logs from the user's device (mock). Tier-2 troubleshooting."""
    return f"Collected VPN logs for {user_email}. Log bundle ID: LOG-8891."


CORE_TOOLS = [search_faq, create_ticket, check_vpn_status, check_email_service_status, lookup_employee]
EXTENDED_TOOLS = CORE_TOOLS + [collect_vpn_logs]


def get_core_tools() -> list:
    return list(CORE_TOOLS)


def get_extended_tools() -> list:
    return list(EXTENDED_TOOLS)


def get_tools_by_name(names: list[str]) -> list:
    by_name = {t.name: t for t in EXTENDED_TOOLS}
    return [by_name[n] for n in names if n in by_name]


TOOL_CATALOG = {
    "search_faq": "Search internal FAQ articles",
    "create_ticket": "Open a support ticket (side effect)",
    "check_vpn_status": "Check VPN health for a user",
    "check_email_service_status": "Check email platform status",
    "lookup_employee": "Fetch employee/device context",
    "collect_vpn_logs": "Collect VPN logs for tier-2 (side effect)",
}


def get_tool_catalog() -> dict:
    return dict(TOOL_CATALOG)
