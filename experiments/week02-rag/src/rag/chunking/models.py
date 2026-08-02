from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class TextChunk:
    index: int
    content: str

    metadata: dict[str, Any] = field(default_factory=dict)