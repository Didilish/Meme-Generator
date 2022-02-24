from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class Pdf_Ingestor(IngestorInterface):
    """Class to pass PDF file and 
    create a list of QuoteModel class.
    """
    allowed_extension = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Subprocess PDF to .txt, 
        Parse .PDF file and create a list 
        of QuoteModel classes.
        
        Returns:
            A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')
            
        quotes = []
        try:
            tmp = f'./_data/DogQuotes/{random.randint(0, 1000)}.txt'
            call = subprocess.call(['pdftotext', path, tmp])
            file_ref = open(tmp, "r")
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0].strip(),
                                           parse[1].strip())
                    quotes.append(new_quote)
            file_ref.close()
            os.remove(tmp)
        except Exception as e:
            raise Exception("pdf parsing issue occured.")
        return quotes