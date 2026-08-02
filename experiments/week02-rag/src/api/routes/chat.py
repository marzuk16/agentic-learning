from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from src.app.dependencies import (
    get_db,
    get_embedding_service,
    get_llm_service,
)
from src.rag.embeddings.base import EmbeddingService
from src.rag.llm.base import LLMService
from src.db.repositories.chunk_repository import ChunkRepository
from src.api.schemas.chat import ChatRequest
from src.rag.services.rag_service import RAGService
from src.rag.services.search_service import SearchService


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "/stream",
)
def chat_stream(
    request: ChatRequest,

    db: Session = Depends(get_db),

    embedding_service: EmbeddingService =
        Depends(get_embedding_service),

    llm_service: LLMService =
        Depends(get_llm_service),
):

    chunk_repository = ChunkRepository(
        db
    )


    search_service = SearchService(
        embedding_service=embedding_service,
        chunk_repository=chunk_repository,
    )


    rag_service = RAGService(
        search_service=search_service,
        llm_service=llm_service,
    )


    return StreamingResponse(
        rag_service.stream_answer(
            request.question
        ),

        media_type="text/plain",
    )
