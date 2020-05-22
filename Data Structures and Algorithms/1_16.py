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

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# TODO
# Filter `mylist` using list comprehension, so that each item > 0
# Filter `mylist` using list comprehension, so that each item < 0


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


if __name__ == '__main__':
    pass
