"""MemeEngine - generates a meme given an image and a quote"""

import os
import random
from PIL import Image
from ..models import QuoteModel
from ..errors import UnsupportedFileError, InputParamsError
import time
from ..utils import out_dir as default_out_dir
from .MemeCaptioner import MemeCaptioner

root_dir = os.path.abspath(os.curdir)
font_path = f'{root_dir}/_data/LilitaOne-Regular.ttf'


class MemeEngine:

    def __init__(self, out_dir: str = default_out_dir):
        """Constructor
        Arguments:
            out_dir {str} - where to save the file
        """
        self.out_dir = out_dir

    def __get_out_file(self, ext):
        filename = f'{int(time.time())}{random.randint(0,1000000)}.{ext}'
        return f'{self.out_dir}/{filename}'

    def make_meme(self, img_path: str, quote: QuoteModel, width: int = 500):
        """Make a meme, given an image and a model
        Arguments:
            :img {str} - the image to load.
            :quote {QuoteModel} -- the model to use.
            :width {int} - the desired width (default 500px)

        Returns:
            str -- path to the saved file which was created
        """

        ext = img_path.split('.')[-1].lower()
        supported_extensions = ["jpg", "png", "jpeg"]

        if ext not in supported_extensions:
            raise UnsupportedFileError("Only jpg and png are supported")

        out_file = self.__get_out_file(ext)
        try:
            with Image.open(img_path) as im:
                # first resize
                w = im.width
                h = im.height
                if w != width:
                    aspect_ratio = w/h
                    im = im.resize((width, int(width/aspect_ratio)))

                # then caption
                MemeCaptioner(im).add_caption(quote)

                # leave off the file format, let the library decide the best
                im.save(root_dir + out_file)

            return out_file
        except OSError as e:
            raise InputParamsError('File IO Error: {}'.format(e))
