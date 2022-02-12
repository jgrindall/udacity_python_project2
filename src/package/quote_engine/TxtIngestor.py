"""Ingest a txt file."""

from .IngestorInterface import IngestorInterface
from typing import List
from ..models import QuoteModel


class TxtIngestor(IngestorInterface):
    """Ingest a txt file."""

    suppported_extensions = ["txt"]

    def __repr__(self) -> str:
        return 'TxtIngestor'

    @classmethod
    def import_and_parse(cls, file: str) -> List[QuoteModel]:
        """Import and parse a txt file

        Arguments:
            file {str} -- the file path.
        Returns:
            List[QuoteModel] -- the quotes

        """
        file_ref = open(file, "r", encoding='utf8', errors='ignore')
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                quotes.append(QuoteModel.from_text(line))
        file_ref.close()
        return quotes
