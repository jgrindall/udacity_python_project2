""" Comment """


import sys
import pandas
from .IngestorInterface import IngestorInterface
from models import QuoteModel
from typing import List

sys.path.append('/models')


class CSVIngestor(IngestorInterface):
    """ Comment """

    suppported_extensions = ["csv"]

    @classmethod
    def import_and_parse(cls, file: str) -> List[QuoteModel]:
        """Import and parse a file

        Arguments:
            file {str} -- the filepath.
        Returns:
            List[QuoteModel] -- the quotes

        """
        df = pandas.read_csv(file, header=0)
        quotes = []
        for index, row in df.iterrows():
            quotes.append(QuoteModel(row['body'], row['author']))
        return quotes
