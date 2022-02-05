"""
Comment
"""

import sys
sys.path.append('/models')

from .TxtIngestor import TxtIngestor
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .IngestorInterface import IngestorInterface
from models import QuoteModel
from typing import List

class Ingestor:

    available_parsers = [TxtIngestor, DocxIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def get_parser(cls, file:str) -> IngestorInterface:
        for Parser in cls.available_parsers:
            if Parser.can_parse(file):
                return Parser

    @classmethod
    def parse(cls, file: str) -> List[QuoteModel]:
        Parser = cls.get_parser(file)
        print(file, Parser)
        if Parser:
            return Parser.import_and_parse(file)
        else:
            raise Exception("No parser found for file")

