"""Command line utility to create memes."""

import os
import random
from quote_engine import Ingestor

root_dir = os.path.abspath(os.curdir)

default_quote_folder = root_dir + '/_data/DogQuotes/'
default_image_folder = root_dir + '/_data/photos/dog/'


def get_random_image():
    """Get one random image"""
    return random.choice(get_all_images())


def get_random_quote():
    """Get one random quote"""
    return random.choice(get_all_quotes())


def memoize_(func):
    """Helper memoisation"""
    cache = dict()
    name = func.__name__

    def memoized_func():
        if name not in cache:
            cache[name] = func()
        return cache[name]
    return memoized_func


@memoize_
def get_all_images():
    """Get all relevant images - memoized"""
    imgs = []
    for root, dirs, files in os.walk(default_image_folder):
        imgs = [os.path.join(root, name) for name in files]
    return imgs


@memoize_
def get_all_quotes():
    """Get all quote models - memoized"""
    quotes = []
    for root, dirs, files in os.walk(default_quote_folder):
        files = [os.path.join(root, name) for name in files]
        for file in files:
            quotes.extend(Ingestor.parse(file))
    return quotes
