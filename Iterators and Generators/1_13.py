"""
*********************************************
**** 4.13. Creating Data Processing Pipelines
*********************************************

#########
# Problem
#########
# You want to process data iteratively in the style of a
# data processing pipeline (similar to Unix pipes).
# For instance, you have a huge amount of data that needs to be processed,
# but it can’t fit entirely into memory

#########
# Solution
#########
# Generator functions are a good way to implement processing pipelines.

# It is important to grasp that the yield statement acts as a kind of data producer
# whereas a for loop acts as a data consumer.

"""


import os
import re
import fnmatch


def gen_find(filepat, top):
    """
    Find all file names in a directory tree that match a shell wildcard pattern
    """
    # Code goes here
    # walk through `top`
    # filter files for `filepat`
    # yield file by joining path and name
    pass


def gen_opener(filenames):
    """
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    """
    # Code goes here
    # yield each file by opening it in `rt` mode
    # close file
    pass


def gen_concatenate(iterators):
    """
    Chain a sequence of iterators together into a single sequence.
    """
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """
    Look for a regex pattern in a sequence of lines.
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


if __name__ == '__main__':
    log_names = gen_find('*.log*', '/Users/chokan/Desktop/slotomotive/slotomotive')
    files = gen_opener(log_names)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    for line in pylines:
        print(line)
