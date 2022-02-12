from abc import ABC, abstractmethod
from ..models import QuoteModel
from typing import List


class IngestorInterface(ABC):

    """Common interface for all ingestors."""

    suppported_extensions = []

    @classmethod
    @abstractmethod
    def import_and_parse(cls, file: str) -> List[QuoteModel]:
        """Override with concrete ways to load and parse files."""
        pass

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Can this parser handle this file?"""
        ext = path.split('.')[-1].lower()
        return ext in cls.suppported_extensions
