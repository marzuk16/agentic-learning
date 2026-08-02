from dataclasses import dataclass
from typing import Any

from src.common.enums import ContentType


@dataclass(slots=True)
class ContentUnit:
    index: int
    content: str

@dataclass(slots=True)
class LoadedDocument:
    title: str
    source: str
    content_type: ContentType
    content_units: list[ContentUnit]
    metadata: dict[str, Any]