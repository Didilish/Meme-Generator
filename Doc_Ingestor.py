"""Class to ingest docx file type."""
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class Doc_Ingestor(IngestorInterface):      
    """Class to parse DOCX file and 
    create a list of QuoteModel class.
    """
    allowed_extension = ['docx']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse DOCX file and create a list 
        of QuoteModel classes.
        
        Returns:
            A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quote_list = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                new_quote = QuoteModel(parse[0], (parse[1]))
                quote_list.append(new_quote)

        return quote_list