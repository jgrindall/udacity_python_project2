"""Ingest PDF."""


from typing import List
import subprocess
from .IngestorInterface import IngestorInterface
from .TxtIngestor import TxtIngestor
from ..models import QuoteModel
from ..utils import get_tmp_file
import os

root_dir = os.path.abspath(os.curdir)


class PDFIngestor(IngestorInterface):

    """Ingest PDF file."""

    suppported_extensions = ['pdf']

    @classmethod
    def import_and_parse(cls, path: str) -> List[QuoteModel]:

        """Import and parse a pdf.
        Arguments:
            :file {str} -- the filepath.
        Returns:
            List[QuoteModel] -- the quotes
        """

        tmp = get_tmp_file()

        """
        We need the `layout` argument to maintain line breaks otherwise lines
        are joined together and it is difficult to split them into quotes.
        """

        cmd = r'{} -enc UTF-8 -layout "{}" "{}"'.format('pdftotext', path, tmp)

        proc = subprocess.Popen(cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        proc.wait()
        (stdout, stderr) = proc.communicate()
        if proc.returncode != 0:
            raise ValueError("Failed to convert pdf to txt")
        else:
            models = TxtIngestor.import_and_parse(tmp)
            os.remove(tmp)
            return models
