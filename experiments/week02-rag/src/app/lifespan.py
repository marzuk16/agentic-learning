from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.rag.embeddings.local import LocalEmbeddingService
from src.rag.llm.local import LocalLLMService


@asynccontextmanager
async def lifespan(app: FastAPI):

    app.state.embedding_service = (
        LocalEmbeddingService()
    )

    app.state.llm_service = (
        LocalLLMService()
    )

    yield

    app.state.embedding_service = None
    app.state.llm_service = None
