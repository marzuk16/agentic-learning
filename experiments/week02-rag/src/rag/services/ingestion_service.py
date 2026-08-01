from pathlib import Path

from sqlalchemy.orm import Session

from src.rag.chunking.base import Chunker
from src.db.models.chunk import Chunk
from src.db.models.document import Document
from src.db.transaction import transaction
from src.rag.embeddings.base import EmbeddingService
from src.rag.ingestion.base import Loader
from src.db.repositories.chunk_repository import ChunkRepository
from src.db.repositories.document_repository import DocumentRepository


class IngestionService:

    def __init__(
        self,
        loader: Loader,
        chunker: Chunker,
        embedding_service: EmbeddingService,
        session: Session,
    ):
        self.loader = loader
        self.chunker = chunker
        self.embedding_service = embedding_service
        self.session = session
        self.document_repository = DocumentRepository(session)
        self.chunk_repository = ChunkRepository(session)


    def ingest_pdf(
        self,
        path: Path,
    ) -> Document:

        with transaction(self.session):

            loaded_document = (
                self.loader.load(path)
            )


            document = Document(
                title=loaded_document.title,
                source=loaded_document.source,
                content_type=loaded_document.content_type,
                metadata_=loaded_document.metadata,
            )


            document = (
                self.document_repository.create(document)
            )


            chunks = (
                self.chunker.chunk(
                    loaded_document
                )
            )


            embeddings = (
                self.embedding_service.embed_many(chunks)
            )


            chunk_entities = []

            for chunk, embedding in zip(
                chunks,
                embeddings,
            ):
                chunk_entities.append(
                    Chunk(
                        document_id=document.id,
                        chunk_index=chunk.index,
                        content=chunk.content,
                        embedding=embedding.vector,
                        metadata_=chunk.metadata,
                    )
                )


            self.chunk_repository.create_many(
                chunk_entities
            )


        return document
