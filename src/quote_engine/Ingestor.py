"""Helper class to read and parse a file using any available ingestor."""

import sys
from .TxtIngestor import TxtIngestor
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .IngestorInterface import IngestorInterface
from models import QuoteModel
from typing import List

sys.path.append('/models')


class Ingestor:

    available_ingestors = [TxtIngestor, DocxIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def get_parser(cls, file: str) -> IngestorInterface:
        """Get the relevant concrete ingestor."""
        for Parser in cls.available_ingestors:
            if Parser.can_parse(file):
                return Parser

    @classmethod
    def parse(cls, file: str) -> List[QuoteModel]:
        """Load and parse a file, returning a list of models"""
        Parser = cls.get_parser(file)
        if Parser:
            return Parser.import_and_parse(file)
        else:
            raise Exception("No parser found for file " + file)
