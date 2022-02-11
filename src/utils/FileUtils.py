"""Command line utility to create memes."""

import os
import random
import time
from ingest import Ingestor

root_dir = os.path.abspath(os.curdir)
out_dir = '/_out'

TEMP_FOLDER = root_dir + '/_tmp'
DEFAULT_QUOTE_FOLDER = root_dir + '/_data/DogQuotes/'
DEFAULT_IMAGE_FOLDER = root_dir + '/_data/photos/dog/'


def get_tmp_file(ext):
    """Get a random temp path."""
    return f'{TEMP_FOLDER}/{int(time.time())}{random.randint(0,1000000)}.{ext}'


def get_random_image():
    """Comment"""
    return random.choice(get_all_images())


def get_random_quote():
    """Comment"""
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
    for root, dirs, files in os.walk(DEFAULT_IMAGE_FOLDER):
        imgs = [os.path.join(root, name) for name in files]
    return imgs


@memoize_
def get_all_quotes():
    """Get all quote models - memoized"""
    quotes = []
    for root, dirs, files in os.walk(DEFAULT_QUOTE_FOLDER):
        files = [os.path.join(root, name) for name in files]
        for file in files:
            quotes.extend(Ingestor.parse(file))
    return quotes
