"""Initialize the QuoteEngine module.

Attributes:
    QuoteModel: Class to hold quote body and author.
    Ingestor: Class that is capable of ingesting multiple files.
    Doc_Ingestor: Class to ingest docx file type.
    Csv_Ingestor: Class to ingest csv file type.
    Pdf_Ingestor: Class to ingest PDF file type.
    Txt_Ingestor: Class to ingest txt file type.

"""
from .Ingestor import Ingestor
from .QuoteModel import QuoteModel

from .Doc_Ingestor import Doc_Ingestor
from .Csv_Ingestor import Csv_Ingestor
from .Pdf_Ingestor import Pdf_Ingestor
from .Txt_Ingestor import Txt_Ingestor
