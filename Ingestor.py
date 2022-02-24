from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from .Doc_Ingestor import Doc_Ingestor
from .Csv_Ingestor import Csv_Ingestor
from .Pdf_Ingestor import Pdf_Ingestor
from .Txt_Ingestor import Txt_Ingestor


class Ingestor(IngestorInterface):
    """Class to encapsulate all the ingestors to 
    provide one interface to load all the file type
    """
    ingestors = [Doc_Ingestor, Csv_Ingestor, Pdf_Ingestor, Txt_Ingestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse to match select an appropriate 
        ingestor to a given file type
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)