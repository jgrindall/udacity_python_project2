""" Comment """
import sys
sys.path.append('/models')

import pandas
from .IngestorInterface import IngestorInterface
from models import QuoteModel
from typing import List


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
        cats = []
        for index, row in df.iterrows():
            new_cat = QuoteModel(row['Name'], row['Age'], row['isIndoor'])
            cats.append(new_cat)
        return cats
