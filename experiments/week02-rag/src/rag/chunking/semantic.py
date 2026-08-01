from src.config import settings
from src.rag.chunking.base import Chunker
from src.rag.chunking.models import TextChunk
from src.rag.ingestion.models import LoadedDocument


class SemanticChunker(Chunker):

    def __init__(
        self,
        chunk_size: int | None = None,
        chunk_overlap: int | None = None,
    ):
        self.chunk_size = (
            chunk_size
            if chunk_size is not None
            else settings.chunk_size
        )
        self.chunk_overlap = (
            chunk_overlap
            if chunk_overlap is not None
            else settings.chunk_overlap
        )


    def chunk(
        self,
        document: LoadedDocument,
    ) -> list[TextChunk]:

        chunks: list[TextChunk] = []

        index = 0

        for unit in document.content_units:

            text_chunks = self._split_text(
                unit.content
            )

            for text in text_chunks:

                chunks.append(
                    TextChunk(
                        index=index,
                        content=text,
                        metadata={
                            "source": document.source,
                            "content_unit": unit.index,
                        },
                    )
                )

                index += 1

        return chunks


    def _split_text(
        self,
        text: str,
    ) -> list[str]:

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk = text[start:end]

            chunks.append(chunk)

            start = end - self.chunk_overlap

        return chunks