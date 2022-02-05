""" Comment """


import sys
import os
import random
from PIL import Image, ImageDraw, ImageFont
from models import QuoteModel
import time
from utils import out_dir

sys.path.append('/models')
sys.path.append('/utils')
root_dir = os.path.abspath(os.curdir)


class MemeEngine:
    """ MemeEngine."""

    def __init__(self, out_path: str=out_dir):
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
            str -- path to the saved file which was created
        """

        out_file = f'{self.out_path}/{int(time.time())}{random.randint(0,1000)}.jpg'

        font_path = f'{root_dir}/_data/LilitaOne-Regular.ttf'
        font = ImageFont.truetype(font_path, size=20)

        with Image.open(img) as im:
            drawer = ImageDraw.Draw(im)
            drawer.multiline_text((10, 10),
                                  quote.get_formatted(),
                                  font=font,
                                  fill=(0, 0, 0))
            im.save(root_dir + out_file, "JPEG")
        return out_file
