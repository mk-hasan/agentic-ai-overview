"""FAQ knowledge used by helpdesk tools and RAG examples."""

FAQ_ENTRIES = {
    "vpn": {
        "title": "VPN disconnects frequently",
        "text": (
            "Restart the VPN client, verify your MFA token, then reconnect to "
            "vpn.corp.example.com. If disconnects continue, collect VPN logs and escalate."
        ),
        "tags": ["vpn", "network", "mfa", "remote"],
    },
    "password": {
        "title": "Password reset",
        "text": (
            "Reset your password at https://sso.example.com/reset (requires MFA). "
            "Wait 5 minutes for sync before retrying locked applications."
        ),
        "tags": ["password", "sso", "login", "mfa"],
    },
    "email": {
        "title": "Outlook issues",
        "text": (
            "Clear Outlook cache (Outlook > Preferences > Storage > Reset) and restart "
            "the app. Check https://status.corp.example.com for service incidents."
        ),
        "tags": ["email", "outlook", "cache", "office"],
    },
    "hardware": {
        "title": "Laptop performance",
        "text": (
            "Run disk cleanup, reboot, and ensure macOS/Windows updates are installed. "
            "Open a ticket if performance issues persist after reboot."
        ),
        "tags": ["laptop", "slow", "hardware", "performance"],
    },
}
