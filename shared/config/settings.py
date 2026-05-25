"""Shared configuration helpers for pattern examples."""

from pathlib import Path

# Repo root (agentic-ai-overview/)
REPO_ROOT = Path(__file__).resolve().parents[2]

# Default env file location
ENV_FILE = REPO_ROOT / ".env"

# Supported LLM providers (every example can use either)
PROVIDERS = ("openai", "deepseek")
DEFAULT_PROVIDER = "openai"

# Example scenarios (use --scenario on any pattern example)
SCENARIOS = ("helpdesk", "ecommerce", "demand-forecast")
DEFAULT_SCENARIO = "helpdesk"

# OpenAI defaults
DEFAULT_OPENAI_MODEL = "gpt-4o-mini"

# DeepSeek defaults (OpenAI-compatible API)
DEFAULT_DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEFAULT_DEEPSEEK_MODEL = "deepseek-chat"

# Backward-compatible alias
DEFAULT_MODEL = DEFAULT_OPENAI_MODEL
