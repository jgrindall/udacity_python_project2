""" Comment """
import sys
sys.path.append('/models')
import re
from .IngestorInterface import IngestorInterface
from typing import List
from models import QuoteModel

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
                parts = re.split(QuoteModel.quote_re_format, line)
                parts = list(filter(lambda s: len(s) >= 1, parts))
                if len(parts) % 2 == 0:
                    i = 0
                    while i < len(parts)/2:
                        quotes.append(QuoteModel(parts[i], parts[i + 1]))
                        i += 2
        file_ref.close()
        return quotes
