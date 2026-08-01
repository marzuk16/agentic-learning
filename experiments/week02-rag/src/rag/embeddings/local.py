from sentence_transformers import SentenceTransformer

from src.config import settings
from src.rag.chunking.models import TextChunk
from src.rag.embeddings.base import EmbeddingService
from src.rag.embeddings.models import Embedding


class LocalEmbeddingService(EmbeddingService):

    def __init__(
        self,
        model_name: str | None = None,
        expected_dim: int | None = None,
    ):
        self.model_name = model_name or settings.embedding_model

        self.model = SentenceTransformer(
            self.model_name
        )

        # The DB vector column has a fixed width (settings.embedding_dim),
        # so the model must produce vectors of exactly that size or every
        # insert/search silently breaks. Fail loudly at startup instead.
        expected = (
            expected_dim
            if expected_dim is not None
            else settings.embedding_dim
        )

        self.dimension = (
            self.model.get_sentence_embedding_dimension()
        )

        if self.dimension != expected:
            raise ValueError(
                f"Embedding model '{self.model_name}' produces "
                f"{self.dimension}-dim vectors, but embedding_dim is "
                f"{expected}. Set EMBEDDING_DIM={self.dimension} and "
                f"recreate the chunks table so the vector column matches."
            )


    def embed(
        self,
        chunk: TextChunk,
    ) -> Embedding:

        vector = self.model.encode(
            chunk.content
        )

        return Embedding(
            vector=vector.tolist(),
            model=self.model_name,
            metadata=chunk.metadata,
        )


    def embed_many(
        self,
        chunks: list[TextChunk],
    ) -> list[Embedding]:

        texts = [
            chunk.content
            for chunk in chunks
        ]

        vectors = self.model.encode(
            texts
        )

        return [
            Embedding(
                vector=vector.tolist(),
                model=self.model_name,
                metadata=chunks[index].metadata,
            )
            for index, vector in enumerate(vectors)
        ]