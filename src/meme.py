"""Command line utility to create memes."""

from package.models import QuoteModel
import argparse
from package.meme_generator import MemeEngine
import traceback
from package.loaders import get_random_image, get_random_quote


class ParamsError(Exception):
    pass


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
        raise ParamsError('Author & body must both be set or both be missing')
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
    except ParamsError as e:
        print("Incorrect params")
    except ValueError as e:
        print("Incorrect params")
    except Exception as e:
        print("Something went wrong")
        print(e)
        print(traceback.format_exc())
