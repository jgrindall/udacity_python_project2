"""Command line utility to create memes."""

import os
import random
from ingest import Ingestor
from models import QuoteModel
import argparse
from engine import MemeEngine

DEFAULT_QUOTE_FOLDER = './_data/DogQuotes/'
DEFAULT_IMAGE_FOLDER = "./_data/photos/dog/"

def get_random_image():
    """Comment"""
    imgs = []
    for root, dirs, files in os.walk(DEFAULT_IMAGE_FOLDER):
        imgs = [os.path.join(root, name) for name in files]
    return random.choice(imgs)

def get_random_quote():
    """Comment"""
    quotes = []
    for root, dirs, files in os.walk(DEFAULT_QUOTE_FOLDER):
        files = [os.path.join(root, name) for name in files]
        for f in files:
            quotes.extend(Ingestor.parse(f))
    return random.choice(quotes)

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None
    img = path if path is not None else get_random_image()
    if body and author:
        quote = QuoteModel(body, author)
    elif not body and not author:
        quote = get_random_quote()
    else:
        raise ValueError('Author and body must both be set or both be missing')
    meme_engine = MemeEngine('./tmp')
    return meme_engine.make_meme(img, quote)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="set a command")
    parser.add_argument('--path', type=str, help="path to an image file (optional)")
    parser.add_argument('--body', type=str, help="quote body to add to the image (optional, required if author is set)")
    parser.add_argument('--author', type=str, help="quote author to add to the image (optional, required if body is set)")
    args = parser.parse_args()
    try:
        print(generate_meme(args.path, args.body, args.author))
    except ValueError as e:
        print("Incorrect params")
        print(e)
    except Exception as e:
        print("Something went wrong")
        print(e)

