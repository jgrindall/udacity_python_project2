"""Comment."""
import sys
import docx
from .IngestorInterface import IngestorInterface
from models import QuoteModel
from typing import List

sys.path.append('/models')


class DocxIngestor(IngestorInterface):

    """Load a docx, split into paragraphs and parse"""

    suppported_extensions = ["docx"]

    @classmethod
    def import_and_parse(cls, file: str) -> List[QuoteModel]:
        """Import and parse a doc.

        Arguments:
            file {str} -- the filepath.
        Returns:
            List[QuoteModel] -- the quotes

        """
        doc = docx.Document(file)
        quotes = []
        for para in doc.paragraphs:
            if para.text != "":
                text = para.text.strip()
                model = QuoteModel.from_text(text)
                quotes.append(model)

        return quotes
