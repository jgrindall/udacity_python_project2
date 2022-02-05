""" Comment."""
import sys
sys.path.append('/models')

from typing import List
import subprocess
import random
from .IngestorInterface import IngestorInterface
from models import QuoteModel


class PDFIngestor(IngestorInterface):

    """Comment."""

    suppported_extensions = ['pdf']

    @classmethod
    def import_and_parse(cls, path: str) -> List[QuoteModel]:

        """Import and parse a pdf.
        Arguments:
            file {str} -- the filepath.
        Returns:
            List[Cat] -- the cats

        """

        tmp = f'./data/{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        print('call', call, path, tmp)

        file_ref = open(tmp, "r")
        cats = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                print(line)
                cat_data = line.split()
                for cat in cat_data:
                    parse = line.split(',')
                    new_cat = Cat(parse[0], int(parse[1]), bool(parse[2]))
                    cats.append(new_cat)

        file_ref.close()

        return cats
