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
            if para.text != "":
                text = para.text.strip()
                # doc quotes must be of the form "body" - author
                matches = re.fullmatch(QuoteModel.quote_re_format, text)
                groups = matches.groups()
                if len(groups) == 2:
                    quotes.append(QuoteModel(groups[0], groups[1]))
                else:
                    raise Exception("doc parse failed")

        return quotes
