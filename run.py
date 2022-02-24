from QuoteEngine import Ingestor
from QuoteEngine import Pdf_Ingestor, Txt_Ingestor
from QuoteEngine import Doc_Ingestor, Csv_Ingestor
#from MemeEngine import MemeEngine

print(Doc_Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
print(Csv_Ingestor.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
print(Pdf_Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
print(Txt_Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))
# print(make_meme('./_data/photos/dog/xander_1.jpg',
# 'Hello', 'Sobaka', 500)
