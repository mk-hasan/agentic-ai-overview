"""Shared LLM client helpers for LangGraph examples."""

import os
from typing import Literal, Optional

from langchain_openai import ChatOpenAI

from shared.config.settings import (
    DEFAULT_DEEPSEEK_BASE_URL,
    DEFAULT_DEEPSEEK_MODEL,
    DEFAULT_OPENAI_MODEL,
    DEFAULT_PROVIDER,
    PROVIDERS,
)
from shared.utils.env import load_env

Provider = Literal["openai", "deepseek"]


def get_openai_chat_model(
    *, model: Optional[str] = None, temperature: float = 0
) -> ChatOpenAI:
    """Return a ChatOpenAI client configured for OpenAI (or OPENAI_BASE_URL override)."""
    load_env()
    kwargs = {
        "model": model or os.getenv("OPENAI_MODEL", DEFAULT_OPENAI_MODEL),
        "temperature": temperature,
    }
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        kwargs["api_key"] = api_key
    base_url = os.getenv("OPENAI_BASE_URL")
    if base_url:
        kwargs["base_url"] = base_url
    return ChatOpenAI(**kwargs)


def get_deepseek_chat_model(
    *, model: Optional[str] = None, temperature: float = 0
) -> ChatOpenAI:
    """Return a ChatOpenAI client configured for the DeepSeek API."""
    load_env()
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError(
            "DEEPSEEK_API_KEY is not set. Add it to .env (see .env.example)."
        )
    return ChatOpenAI(
        model=model or os.getenv("DEEPSEEK_MODEL", DEFAULT_DEEPSEEK_MODEL),
        api_key=api_key,
        base_url=os.getenv("DEEPSEEK_BASE_URL", DEFAULT_DEEPSEEK_BASE_URL),
        temperature=temperature,
    )


def get_chat_model(
    *,
    provider: Optional[str] = None,
    model: Optional[str] = None,
    temperature: float = 0,
) -> ChatOpenAI:
    """Return a chat model for the given provider (`openai` or `deepseek`)."""
    load_env()
    selected = (provider or os.getenv("DEFAULT_PROVIDER", DEFAULT_PROVIDER)).lower()
    if selected == "openai":
        return get_openai_chat_model(model=model, temperature=temperature)
    if selected == "deepseek":
        return get_deepseek_chat_model(model=model, temperature=temperature)
    raise ValueError(f"Unknown provider {selected!r}. Choose from: {', '.join(PROVIDERS)}")
