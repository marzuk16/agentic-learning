from fastapi import Request

from src.db.database import get_db
from src.rag.embeddings.base import EmbeddingService

from src.rag.llm.base import LLMService

__all__ = [
    "get_db",
    "get_embedding_service",
    "get_llm_service",
]


def get_embedding_service(
    request: Request,
) -> EmbeddingService:

    return request.app.state.embedding_service

def get_llm_service(
    request: Request,
) -> LLMService:

    return request.app.state.llm_service