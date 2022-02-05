"""Comment."""
import sys
import docx
from .IngestorInterface import IngestorInterface
from models import QuoteModel
from typing import List
import re

sys.path.append('/models')


class DocxIngestor(IngestorInterface):

    """Comment"""

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
            print(para.text)
            if para.text != "":
                text = para.text.strip()
                # doc quotes must be of the form "body" - author
                result = re.search(QuoteModel.quote_re_format, text)
                quotes.append(QuoteModel(result.group(1), result.group(2)))

        return quotes
