import os
from package.loaders import get_random_image, get_random_quote, get_all_images, get_all_quotes

root_dir = os.path.abspath(os.curdir)

if __name__ == "__main__":
    print('root_dir', root_dir)
    print('get_all_images', get_all_images())
    print('get_all_quotes', get_all_quotes())
    print('get_random_image', get_random_image())
    print('get_random_quote', get_random_quote())
