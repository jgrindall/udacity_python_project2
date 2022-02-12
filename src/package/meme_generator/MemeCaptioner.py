"""MemeCaptioner - handles adding captions"""

import os
import random
from PIL import ImageDraw, ImageFont
from ..models import QuoteModel

root_dir = os.path.abspath(os.curdir)
font_path = f'{root_dir}/_data/LilitaOne-Regular.ttf'


class MemeCaptioner:

    def __init__(self, img):
        """Constructor
        Arguments:
            img {Image} - the Pillow image to add a caption to
        """
        self.img = img

    @staticmethod
    def get_color():
        "Get a random color."
        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))

    def add_caption(self, quote: QuoteModel):
        """Draw a meme, into the image
        Arguments:
            quote {QuoteModel} -- the model to use.
        Returns the same image, with a caption added
        """

        # some randomisation of colors etc
        font_size = random.randint(16, 32)
        font = ImageFont.truetype(font_path, size=font_size)
        font_x = random.randint(8, 32)
        font_y = random.randint(8, 200)

        drawer = ImageDraw.Draw(self.img)
        drawer.multiline_text((font_x, font_y),
                              quote.get_formatted(),
                              font=font,
                              fill=self.get_color())

        return self.img
