""" Comment """

import sys
from abc import ABC, abstractmethod
from models import QuoteModel
from typing import List

sys.path.append('/models')


class IngestorInterface(ABC):

    """ Comment."""

    suppported_extensions = []

    @classmethod
    @abstractmethod
    def import_and_parse(cls, file: str) -> List[QuoteModel]:
        """ Comment."""
        pass

    @classmethod
    def can_parse(cls, path):
        """ Comment."""
        ext = path.split('.')[-1]
        return ext in cls.suppported_extensions
