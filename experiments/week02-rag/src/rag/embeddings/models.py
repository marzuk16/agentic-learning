from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Embedding:
    vector: list[float]
    model: str

    metadata: dict[str, Any] = field(default_factory=dict)