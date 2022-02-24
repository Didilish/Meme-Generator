"""Class to ingest Text file type"""
from typing import List
import subprocess
import os

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class Txt_Ingestor(IngestorInterface):
    """Class to parse TEXT file and
    create a list of QuoteModel class.
    """
    allowed_extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse TEXT file and create a list
        of QuoteModel classes.

        Returns:
            A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes_list = []

        try:
            file_ref = open(path, "r")
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes_list.append(new_quote)

            file_ref.close()
        except Exception as e:
            raise Exception("txt parsing issue occured.")
        return quotes_list
