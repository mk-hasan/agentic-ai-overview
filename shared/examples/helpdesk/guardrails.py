"""Guardrail helpers for helpdesk examples."""

import re

PII_PATTERNS = [
    (re.compile(r"\b\d{3}-\d{2}-\d{4}\b"), "SSN-like number"),
    (re.compile(r"\b\d{16}\b"), "credit-card-like number"),
    (re.compile(r"\b\d{3}-\d{3}-\d{4}\b"), "phone number"),
]

BLOCKED_REQUESTS = [
    "disable antivirus",
    "share admin password",
    "bypass mfa",
    "turn off encryption",
]


def scan_for_pii(text: str) -> list[str]:
    findings = []
    for pattern, label in PII_PATTERNS:
        if pattern.search(text):
            findings.append(label)
    return findings


def scan_for_policy_violations(text: str) -> list[str]:
    lower = text.lower()
    return [phrase for phrase in BLOCKED_REQUESTS if phrase in lower]


def validate_ticket(title: str, description: str) -> tuple[bool, str]:
    combined = f"{title}\n{description}"
    pii = scan_for_pii(combined)
    if pii:
        return False, f"Ticket rejected: remove sensitive data ({', '.join(pii)})."
    if not title.strip() or not description.strip():
        return False, "Ticket rejected: title and description are required."
    return True, "ok"
