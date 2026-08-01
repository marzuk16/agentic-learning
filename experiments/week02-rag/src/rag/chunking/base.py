from abc import ABC, abstractmethod

from src.rag.chunking.models import TextChunk
from src.rag.ingestion.models import LoadedDocument


class Chunker(ABC):

    @abstractmethod
    def chunk(
        self,
        document: LoadedDocument,
    ) -> list[TextChunk]:
        raise NotImplementedError