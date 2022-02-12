"""Command line utility to create memes."""

import os
import random
import time

root_dir = os.path.abspath(os.curdir)
out_dir = '/_out'
temp_folder = root_dir + '/_tmp'


def get_tmp_file(ext: str = "txt"):
    """Get a random temp path.
        Arguments:
        :ext - the extension you want to use. Eg. txt
        """
    return f'{temp_folder}/{int(time.time())}{random.randint(0,1000000)}.{ext}'
