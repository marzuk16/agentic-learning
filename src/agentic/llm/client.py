"""LLM client wired to configuration.

Builds an OpenAI-compatible client from `settings` (local MLX server by
default) so nothing here is hardcoded — point it at a different endpoint or
model purely via `.env`.
"""

from openai import OpenAI

from agentic.config.constants import Roles
from agentic.config.settings import Settings, get_settings


def build_client(settings: Settings | None = None) -> OpenAI:
    """Create an OpenAI client from settings.

    Pass an explicit `settings` for tests; otherwise the cached singleton is used.
    """
    settings = settings or get_settings()
    return OpenAI(
        base_url=settings.llm_base_url,
        api_key=settings.llm_api_key,
    )


def chat(
    prompt: str,
    system: str | None = None,
    *,
    settings: Settings | None = None,
) -> str:
    """Send a single prompt and return the assistant's reply text."""
    settings = settings or get_settings()
    client = build_client(settings)

    messages: list[dict[str, str]] = []
    if system:
        messages.append({"role": Roles.SYSTEM, "content": system})
    messages.append({"role": Roles.USER, "content": prompt})

    response = client.chat.completions.create(
        model=settings.model_name,
        messages=messages,
    )
    return response.choices[0].message.content or ""


if __name__ == "__main__":
    print(chat("Write Hello World in Python"))
