"""
************************************************************
**** 1.16.  Filtering Sequence Elements
************************************************************


#########
# Problem
#########
# You have data inside of a sequence,
# and need to extract values or reduce the sequence using some criteria.


#########
# Solution
#########
# The easiest way to filter sequence data is often to use a list comprehension.
"""

import math
from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# TODO
# Filter `mylist` using list comprehension, so that each item > 0
# Filter `mylist` using list comprehension, so that each item < 0
# Filter `mylist` using list comprehension, so that each item > 0 and return vals are `sqrt`


# One potential downside of using a list comprehension
# is that it might produce a large result if the original input is large.

# TODO
# Use generator expression to produce filtered values iteratively

# If filtering criteria cannot be easily expressed in a list comprehension or generator expression.
# Use built-in 'filter()' function

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

# TODO
# Create a function that takes an arg and returns `bool` is it `int` or not
# Use built-in `filter` and newly created functions to filter `values above`

# TODO
# Filter `mylist` use: list comprehension, if/else statements so that if n > 0 add val else add 0


# You’re trying to apply the results of filtering one sequence to another related sequence.
# Suppose you have the following two columns of data:

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

# Now suppose you want to make a list of all addresses
# where the corresponding count value was greater than 5.

# TODO
# Filter counts so that if each val in output is > 5 will have True bool
# Use `compress()` filtering tool


if __name__ == '__main__':
    pass
