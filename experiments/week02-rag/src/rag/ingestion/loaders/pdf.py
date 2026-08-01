from pathlib import Path

import fitz

from src.common.enums import ContentType
from src.rag.ingestion.base import Loader
from src.rag.ingestion.models import ContentUnit, LoadedDocument


class PDFLoader(Loader):

    def load(self, source: Path) -> LoadedDocument:
        document = fitz.open(source)

        metadata = dict(document.metadata or {})

        content_units: list[ContentUnit] = []

        for page_number, page in enumerate(document, start=1):
            text = page.get_text().strip()

            if not text:
                continue

            content_units.append(
                ContentUnit(
                    index=page_number,
                    content=text,
                )
            )

        return LoadedDocument(
            title=metadata.get("title") or source.stem,
            source=str(source),
            content_type=ContentType.PDF,
            content_units=content_units,
            metadata=metadata,
        )