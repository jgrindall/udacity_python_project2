"""Command line utility to create memes."""

import os
import random
from ingest import Ingestor

root_dir = os.path.abspath(os.curdir)
DEFAULT_QUOTE_FOLDER = root_dir + '/src/_data/DogQuotes/'
DEFAULT_IMAGE_FOLDER = root_dir + '/src/_data/photos/dog/'


def get_random_image():
    """Comment"""
    return random.choice(get_all_images())


def get_random_quote():
    """Comment"""
    return random.choice(get_all_quotes())


def memoize_(func):
    cache = dict()
    name = func.__name__

    def memoized_func():
        if name not in cache:
            cache[name] = func()
        return cache[name]
    return memoized_func


@memoize_
def get_all_images():
    """Comment"""
    imgs = []
    for root, dirs, files in os.walk(DEFAULT_IMAGE_FOLDER):
        imgs = [os.path.join(root, name) for name in files]
    return imgs


@memoize_
def get_all_quotes():
    """Comment"""
    quotes = []
    for root, dirs, files in os.walk(DEFAULT_QUOTE_FOLDER):
        files = [os.path.join(root, name) for name in files]
        for f in files:
            quotes.extend(Ingestor.parse(f))
    return quotes
