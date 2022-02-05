import os
import requests
from flask import Flask, render_template, abort, request
from engine import MemeEngine
from utils import get_random_image, get_random_quote, get_all_quotes, get_all_images, out_dir

meme_engine = MemeEngine()
root_dir = os.path.abspath(os.curdir)
quotes = get_all_quotes()
imgs = get_all_images()

app = Flask(__name__, static_folder=root_dir + out_dir)

@app.route('/')
def meme_rand():
    """ Generate a random meme """
    path_generated = meme_engine.make_meme(get_random_image(), get_random_quote())
    return render_template('meme.html', path=path_generated)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    path = None

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
