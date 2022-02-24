from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Class to implement a can_ingest class method"""
    allowed_extension = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Determine if class can ingest this file type."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse to implement interface in the children classes"""
        pass
