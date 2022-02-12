"""Helper class to read and parse a file using any available ingestor."""

from .TxtIngestor import TxtIngestor
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .IngestorInterface import IngestorInterface
from ..models import QuoteModel
from typing import List
from ..errors import UnsupportedFileError


class Ingestor:

    available_ingestors = [TxtIngestor, DocxIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def get_parser(cls, file: str) -> IngestorInterface:
        """Get the relevant concrete ingestor.
        Test creating basic model
        >>> print(Ingestor.get_parser("something.pdf"))
        PDFIngestor
        """
        for Parser in cls.available_ingestors:
            if Parser.can_ingest(file):
                return Parser

    @classmethod
    def parse(cls, file: str) -> List[QuoteModel]:
        """Load and parse a file, returning a list of models"""
        Parser = cls.get_parser(file)
        if Parser:
            return Parser.import_and_parse(file)
        else:
            raise UnsupportedFileError("No parser found for file " + file)
