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
font_path = f'{root_dir}/_data/LilitaOne-Regular.ttf'



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
            img {str} - the image to load.
            quote {QuoteModel} -- the model to use.

        Returns:
            str -- path to the saved file which was created
        """

        out_file = f'{self.out_path}/{int(time.time())}{random.randint(0,1000)}.jpg'
        font_size = random.randint(16, 32)
        font = ImageFont.truetype(font_path, size=font_size)
        font_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        font_x = random.randint(8, 32)
        font_y = random.randint(8, 200)
        
        with Image.open(img) as im:
            drawer = ImageDraw.Draw(im)
            drawer.multiline_text((font_x, font_y),
                                  quote.get_formatted(),
                                  font=font,
                                  fill=font_color)
            im.save(root_dir + out_file, "JPEG")
        return out_file
