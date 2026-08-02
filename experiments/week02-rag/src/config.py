from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # LLM
    llm_base_url: str
    llm_api_key: str
    llm_model: str

    # Database
    debug: bool = False
    database_url: str
    database_echo: bool | None = Field(default=None)

    # Redis
    redis_url: str

    # Embeddings
    embedding_model: str = "BAAI/bge-small-en-v1.5"
    embedding_dim: int = 384

    # RAG
    chunk_size: int = 500
    chunk_overlap: int = 50
    top_k: int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()