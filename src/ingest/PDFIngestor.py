""" Comment."""


import sys
from typing import List
import subprocess
import random
from .IngestorInterface import IngestorInterface
from .TxtIngestor import TxtIngestor
from models import QuoteModel
import os
import time

root_dir = os.path.abspath(os.curdir)
sys.path.append('/models')
TEMP_FOLDER = root_dir + '/_tmp/'


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

        tmp = f'{TEMP_FOLDER}/{int(time.time())}{random.randint(0,1000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        return TxtIngestor.import_and_parse(tmp)
