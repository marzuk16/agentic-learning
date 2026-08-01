from src.config import settings
from src.rag.chunking.models import TextChunk
from src.rag.embeddings.base import EmbeddingService
from src.db.repositories.chunk_repository import ChunkRepository


class SearchService:

    def __init__(
        self,
        embedding_service: EmbeddingService,
        chunk_repository: ChunkRepository,
        top_k: int | None = None,
    ):
        self.embedding_service = embedding_service
        self.chunk_repository = chunk_repository
        self.top_k = (
            top_k
            if top_k is not None
            else settings.top_k
        )


    def search(
        self,
        query: str,
        limit: int | None = None,
    ):

        limit = (
            limit
            if limit is not None
            else self.top_k
        )

        query_chunk = TextChunk(
            index=0,
            content=query,
        )


        embedding = (
            self.embedding_service.embed(
                query_chunk
            )
        )


        return (
            self.chunk_repository
            .similarity_search(
                embedding.vector,
                limit,
            )
        )