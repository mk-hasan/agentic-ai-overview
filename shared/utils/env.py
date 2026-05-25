"""Load environment variables from the repo root `.env` file."""

from dotenv import load_dotenv

from shared.config.settings import ENV_FILE

_loaded = False


def load_env() -> None:
    global _loaded
    if not _loaded:
        load_dotenv(ENV_FILE)
        _loaded = True
