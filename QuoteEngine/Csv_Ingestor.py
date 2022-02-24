"""Class to ingest CSV file type"""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class Csv_Ingestor(IngestorInterface):
    """Class to parse CSV file and
    create a list of QuoteModel class.
    """
    allowed_extension = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV file and create a list
        of QuoteModel classes.

        Returns:
            A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes_list = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes_list.append(new_quote)

        return quotes_list
