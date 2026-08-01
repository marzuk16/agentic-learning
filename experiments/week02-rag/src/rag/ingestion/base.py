from abc import ABC, abstractmethod
from pathlib import Path

from src.rag.ingestion.models import LoadedDocument


class Loader(ABC):

    @abstractmethod
    def load(self, source: Path) -> LoadedDocument:
        pass