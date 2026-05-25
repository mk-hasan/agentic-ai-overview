"""Tests for helpdesk mock tools."""

from shared.examples.helpdesk.tools import create_ticket, search_faq


def test_search_faq_finds_vpn_article():
    result = search_faq.invoke({"query": "vpn disconnect"})
    assert "vpn" in result.lower()


def test_create_ticket_rejects_empty_title():
    result = create_ticket.invoke({"title": "", "description": "test", "priority": "low"})
    assert "Ticket rejected" in result


def test_create_ticket_success():
    result = create_ticket.invoke(
        {
            "title": "VPN drops",
            "description": "User loses VPN every hour",
            "priority": "high",
        }
    )
    assert "Ticket created" in result
    assert "INC-" in result
