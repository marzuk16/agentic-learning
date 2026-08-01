import tempfile
from pathlib import Path

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from src.app.dependencies import (
    get_db,
    get_embedding_service,
)
from src.rag.chunking.semantic import SemanticChunker
from src.rag.embeddings.base import EmbeddingService
from src.rag.ingestion.loaders.pdf import PDFLoader
from src.rag.services.ingestion_service import IngestionService


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    embedding_service: EmbeddingService =
        Depends(get_embedding_service),
):

    service = IngestionService(
        loader=PDFLoader(),
        chunker=SemanticChunker(),
        embedding_service=embedding_service,
        session=db,
    )

    filename = Path(file.filename or "document.pdf").name

    tmp_dir = Path(tempfile.mkdtemp())
    tmp_path = tmp_dir / filename

    tmp_path.write_bytes(await file.read())

    try:
        document = service.ingest_pdf(tmp_path)
    finally:
        tmp_path.unlink(missing_ok=True)
        tmp_dir.rmdir()

    return {
        "id": str(document.id),
        "title": document.title,
        "source": document.source,
        "content_type": document.content_type.value,
    }
