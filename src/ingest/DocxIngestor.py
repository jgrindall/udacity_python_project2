"""Comment."""
import sys
sys.path.append('/models')

import docx
from .IngestorInterface import IngestorInterface
from models import QuoteModel
from typing import List

class DocxIngestor(IngestorInterface):

    """Comment"""

    suppported_extensions = ["docx"]

    @classmethod
    def import_and_parse(cls, file: str) -> List[QuoteModel]:
        """Import and parse a doc.

        Arguments:
            file {str} -- the filepath.
        Returns:
            List[Cat] -- the quotes

        """
        doc = docx.Document(file)
        cats = []
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(',')
                new_cat = QuoteModel(parse[0], int(parse[1]), bool(parse[2]))
                cats.append(new_cat)

        return cats
