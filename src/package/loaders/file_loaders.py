"""Command line utility to create memes."""

import os
import random
from ..quote_engine import Ingestor

root_dir = os.path.abspath(os.curdir)

default_quote_folder = root_dir + '/_data/DogQuotes/'
default_image_folder = root_dir + '/_data/photos/'

print('using default_quote_folder', default_quote_folder)
print('using default_image_folder', default_image_folder)


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
        paths = [os.path.join(root, name) for name in files]
        print('found images:', root, files)
        print('paths', paths, '\n')
        for path in paths:
            imgs.append(path)
    return imgs


@memoize_
def get_all_quotes():
    """Get all quote models - memoized"""
    quotes = []
    for root, dirs, files in os.walk(default_quote_folder):
        paths = [os.path.join(root, name) for name in files]
        print('found images:', root, files)
        print('paths', paths, '\n')
        for path in paths:
            quotes.extend(Ingestor.parse(path))
    return quotes
