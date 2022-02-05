""" Comment """


import sys
import os
import requests
import random
import subprocess
from PIL import Image, ImageDraw, ImageFont
from models import QuoteModel

sys.path.append('/models')
root = os.path.abspath(os.curdir)


class MemeEngine:
    """ MemeEngine."""

    def __init__(self, out_path: str):
        """Constructor
        Arguments:
            out_path {str} - where to save
        """
        self.out_path = out_path

    def make_meme(self, img, quote: QuoteModel):
        """Make a meme, give a model
        Arguments:
            quote {QuoteModel} -- the model.
            img {str} - the image to load
        Returns:
            str -- TODO
        """

        out_file = f'{self.out_path}/{random.randint(0,100000000)}.jpg'

        print(img, quote, self.out_path, out_file)

        font_path = f'{root}/LilitaOne-Regular.ttf'
        font = ImageFont.truetype(font_path, size=20)

        with Image.open(img) as im:
            drawer = ImageDraw.Draw(im)
            drawer.multiline_text((10, 10), quote.get_formatted(),
                                  font=font, fill=(0, 0, 0))
            im.save(out_file, "JPEG")

        return out_file
