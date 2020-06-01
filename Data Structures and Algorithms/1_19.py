"""
************************************************************
**** 1.19.  Transforming and Reducing Data at the Same Time
************************************************************


#########
# Problem
#########
# You need to execute a reduction function (e.g., sum(), min(), max()),
# but first need to transform or filter the data.


#########
# Solution
#########
# A very elegant way to combine a data reduction and a transformation
# is to use a generator-expression argument.
"""

import os

nums = [1, 2, 3, 4, 5]
# TODO
# Make a generator expr sqrt of each item in nums
# Sum the generator above
# The above 2 step method was `not elegant` use `elegant` way
# Introduce an extra step that creates an extra `list` instead use of `generator`

# INFO
# For such a small list(`nums`), it might not matter, but if `nums` was huge,
# you would end up creating a large temporary data structure to only be used once and discarded.
# The generator solution transforms the data iteratively and is therefore much more memory-efficient.

files = os.listdir('/Users/chokan/Desktop/software engineering/python/Data Structures and Algorithms')
# TODO
# Determine if `any` .py files exist in a directory using python `generator` expr
# Just print out python/not python file


s = ('ACME', 50, 123.45)
# TODO
# Output a tuple as CSV
# HINT: just `join` them


portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
# TODO
# Find the `min` of portfolio shares using generator expression
# Again using a `generator` expr, but this time use lambda to find min share.
# See the diff of two approaches above (for loop/lambda)


if __name__ == '__main__':
    pass
