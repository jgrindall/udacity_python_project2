"""Load a CSV file and use pandas to parse."""

import pandas
from .IngestorInterface import IngestorInterface
from ..models import QuoteModel
from typing import List


class CSVIngestor(IngestorInterface):
    """Load and parse a CSV file."""

    suppported_extensions = ["csv"]

    def __repr__(self) -> str:
        return 'CSVIngestor'

    @classmethod
    def import_and_parse(cls, file: str) -> List[QuoteModel]:
        """Import and parse a csv file

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
