""" Comment """

import sys
from .IngestorInterface import IngestorInterface
from typing import List
from models import QuoteModel

sys.path.append('/models')


class TxtIngestor(IngestorInterface):
    """ Comment """

    suppported_extensions = ["txt"]

    @classmethod
    def import_and_parse(cls, file: str) -> List[QuoteModel]:
        """Import and parse a file

        Arguments:
            file {str} -- the filepath.
        Returns:
            List[QuoteModel] -- the quotes

        """
        file_ref = open(file, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                quotes.append(QuoteModel.from_text(line))
        file_ref.close()
        return quotes
