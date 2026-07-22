"""Fixed string constants used across the app.

These never change between environments. If a value differs between
dev/staging/prod (hosts, ports, secrets), it belongs in `settings.py`, not here.
"""

from enum import StrEnum

# --- Simple constants ---------------------------------------------------------
APP_TITLE = "Agentic Learning Platform"
DEFAULT_ENCODING = "utf-8"

# --- Grouped / namespaced constants ------------------------------------------
# Grouping under a frozen class avoids polluting the module namespace and
# reads nicely at the call site: Tables.CONVERSATIONS


class Tables:
    CONVERSATIONS = "conversations"
    MESSAGES = "messages"
    EMBEDDINGS = "embeddings"


class Roles:
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


# --- StrEnum for a closed set of related values ------------------------------
# Use this when the values are a fixed vocabulary you'll validate against.
class ModelProvider(StrEnum):
    MLX = "mlx"
    OPENAI = "openai"


# --- Error / log message templates -------------------------------------------
class Messages:
    MODEL_NOT_FOUND = "Model '{name}' was not found for provider '{provider}'."
    EMPTY_PROMPT = "Prompt must not be empty."
