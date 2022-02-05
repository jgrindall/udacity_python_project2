"""Comment."""

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

    available_parsers = [TxtIngestor, DocxIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def get_parser(cls, file: str) -> IngestorInterface:
        """Comment."""
        for Parser in cls.available_parsers:
            if Parser.can_parse(file):
                return Parser

    @classmethod
    def parse(cls, file: str) -> List[QuoteModel]:
        """Comment."""
        Parser = cls.get_parser(file)
        if Parser:
            return Parser.import_and_parse(file)
        else:
            raise Exception("No parser found for file")
