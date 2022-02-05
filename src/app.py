import random
import os
import requests
from flask import Flask, render_template, abort, request
from engine import MemeEngine
from ingest import Ingestor
from utils import get_random_image, get_random_quote, get_all_quotes, get_all_images

app = Flask(__name__, static_url_path='', static_folder='./_out')

meme_engine = MemeEngine()

quotes = get_all_quotes()
imgs = get_all_images()

@app.route('/')
def meme_rand():

    """ Generate a random meme """
    print(get_random_image(), get_random_quote())
    path = meme_engine.make_meme(get_random_image(), get_random_quote())
    print(path)
    
    print(os.path.basename(path))
    
    
    return render_template('meme.html', path=os.path.basename(path))


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
