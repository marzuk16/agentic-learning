"""Runtime configuration loaded from environment / `.env`.

Everything here can vary per environment. Values are read from environment
variables (or a local `.env` file) and validated by pydantic. Import the
singleton `settings` object anywhere you need a value.
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from agentic.config.constants import ModelProvider


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "agentic-learning"

    # Postgres
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "agentic_db"
    postgres_user: str = "agentic_user"
    postgres_password: str = Field(default="", repr=False)  # hide secret in logs

    # Redis
    redis_host: str = "localhost"
    redis_port: int = 6379

    # LLM — OpenAI-compatible endpoint (local MLX server by default)
    model_provider: ModelProvider = ModelProvider.MLX
    model_name: str = "mlx-community/Qwen3-8B-4bit"
    llm_base_url: str = "http://127.0.0.1:8080/v1"
    llm_api_key: str = Field(default="none", repr=False)  # hide secret in logs

    @property
    def postgres_dsn(self) -> str:
        return (
            f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


@lru_cache
def get_settings() -> Settings:
    """Cached accessor so the `.env` file is parsed only once."""
    return Settings()


# Convenience singleton for simple imports: `from ...settings import settings`
settings = get_settings()
