"""Command line utility to create memes."""

from package.models import QuoteModel
import argparse
from package.meme_generator import MemeEngine
from package.errors import InputParamsError, UnsupportedFileError, ParseError
import traceback
from package.loaders import get_random_image, get_random_quote


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
        raise InputParamsError('Author & body must both be set or both be missing')
    return MemeEngine().make_meme(img, quote)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="set a command")
    parser.add_argument('--path', type=str,
                        help="path to an image file (optional)")
    parser.add_argument('--body', type=str,
                        help=("quote body to add to the image"
                              "(optional, required if author is set)"))
    parser.add_argument('--author', type=str,
                        help=("quote author to add to the image"
                              "(optional, required if body is set)"))
    args = parser.parse_args()

    try:
        print(generate_meme(args.path, args.body, args.author))
    except InputParamsError as e:
        print('Input Params Error: {}'.format(e))
    except UnsupportedFileError as e:
        print('Unsupported File Error: {}'.format(e))
    except ParseError as e:
        print('Parse Error: {}'.format(e))
    except Exception as e:
        print('Unexpected Error: {}'.format(e))

