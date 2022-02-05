""" Comment """
import sys
sys.path.append('/models')

import requests
import random
import subprocess
from PIL import Image, ImageDraw, ImageFont
from models import QuoteModel


class MemeEngine:
    """ MemeEngine """
    
    @classmethod
    def make_meme(cls, img, quote: QuoteModel):
        """Make a meme, give a model
        Arguments:
            quote {QuoteModel} -- the model.
            img {str}
        Returns:
            str -- TODO
        """
        
        print(img, quote)
        
        """crop = None
        params = (crop["left"], crop["top"], crop["left"] + crop["width"], crop["top"] + crop["height"])
        im_crop = im.crop(params)
        aspect_ratio = crop["width"]/crop["height"]
        im_resized = im_crop.resize((width, int(width/aspect_ratio)))
        font_path = './data/LilitaOne-Regular.ttf'
        font = ImageFont.truetype(font_path, size=20)
        d = ImageDraw.Draw(im_resized)
        d.multiline_text((10, 10), "Hello\nWorld", font=font, fill=(0, 0, 0))
        im_resized.save(out_path, "JPEG")"""

        return "abc"
