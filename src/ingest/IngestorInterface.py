""" Comment """

import sys
sys.path.append('/models')

from abc import ABC, abstractmethod
from models import QuoteModel

from typing import List

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
