from abc import ABC, abstractmethod

from src.rag.chunking.models import TextChunk
from src.rag.embeddings.models import Embedding


class EmbeddingService(ABC):

    @abstractmethod
    def embed(
        self,
        chunk: TextChunk,
    ) -> Embedding:
        raise NotImplementedError

    @abstractmethod
    def embed_many(
        self,
        chunks: list[TextChunk],
    ) -> list[Embedding]:
        raise NotImplementedError