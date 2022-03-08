from PIL import Image, ImageDraw, ImageFont
from random import randint
import os
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
import textwrap


class MemeEngine():
    """A class for creating memes out of images and quotes."""

    def __init__(self, output_dir='output'):
        """Create an instance of this class.
        :param output_dir: A string path to the directory to output files to.
        """
        os.makedirs(output_dir, exist_ok=True)
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a new meme.
        Attributes:
        img_path: path of the image
        text: quote for the meme
        author: author of the quote
        width: width of the meme image - set to 500

        Return: path of the meme
        """
        # load image
        img = Image.open(img_path)
        
        # Resize image
        if not width:
            width = 500
        height = int(width / float(img.size[0]) * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        # draw text    
        message = text + "\n - " + author
        wrapper = textwrap.TextWrapper(width=50)
        message = wrapper.fill(text=message)
        
        if message is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(
                            './font/LilitaOne-Regular.ttf',
                            size=20)
                        
            draw.text((2, 2), text, font=font)
            draw.text((30, 30), author, font=font)

        path = f'{self.output_dir}/{randint(0,100000000)}.jpeg'

        # Save
        img.save(path)
        return path
