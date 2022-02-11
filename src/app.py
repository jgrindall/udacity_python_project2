import os
import requests
from models import QuoteModel
from flask import Flask, render_template, request, abort
from engine import MemeEngine
from loaders import get_random_image, get_random_quote
from utils import get_tmp_file, out_dir

meme_engine = MemeEngine()
root_dir = os.path.abspath(os.curdir)

# Serve static images from root_dir + out_dir
app = Flask(__name__, static_folder=root_dir + out_dir)


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    path_generated = meme_engine.make_meme(
        get_random_image(),
        get_random_quote())
    return render_template('meme.html', path=path_generated)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form.get('image_url', "").strip()
    body = request.form.get('body', "").strip()
    author = request.form.get('author', "").strip()

    if not image_url or not body or not author:
        abort(400, "Please include an image, a body and an author")

    ext = image_url.split('.')[-1].lower()
    supported_extensions = ["jpg", "png", "jpeg"]

    if ext not in supported_extensions:
        abort(422, "Only jpg and png are currently supported")

    tmp = get_tmp_file(ext)
    load_request = requests.get(image_url)

    with open(tmp, 'wb') as img:
        img.write(load_request.content)
    out_path = meme_engine.make_meme(tmp, QuoteModel(body, author))

    os.remove(tmp)
    return render_template('meme.html', path=out_path)


if __name__ == "__main__":
    app.run()
