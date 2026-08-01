from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from src.app.dependencies import get_db
from src.rag.embeddings.base import EmbeddingService
from src.app.dependencies import get_embedding_service

from src.db.repositories.chunk_repository import ChunkRepository
from src.rag.services.search_service import SearchService

from src.api.schemas.search import (
    SearchRequest,
    SearchResponse,
    SearchResult,
)


router = APIRouter(
    prefix="/search",
    tags=["Search"],
)


@router.post(
    "",
    response_model=SearchResponse,
)
def search(
    request: SearchRequest,
    db: Session = Depends(get_db),
    embedding_service: EmbeddingService = Depends(
        get_embedding_service
    ),
):

    chunk_repository = ChunkRepository(
        db
    )

    search_service = SearchService(
        embedding_service=embedding_service,
        chunk_repository=chunk_repository,
    )


    chunks = search_service.search(
        query=request.query,
        limit=request.limit,
    )


    return SearchResponse(
        results=[
            SearchResult(
                id=str(chunk.id),
                content=chunk.content,
                metadata=chunk.metadata_,
            )
            for chunk in chunks
        ]
    )