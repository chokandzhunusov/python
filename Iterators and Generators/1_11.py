"""
***********************************************************
**** 4.11. Iterating Over Multiple Sequences Simultaneously
***********************************************************

#########
# Problem
#########
# You want to iterate over the items contained in more than one sequence at a time.

#########
# Solution
#########
# To iterate over more than one sequence simultaneously, use the `zip()` function.
# NOTE: it’s important to emphasize that `zip()` creates an iterator as a result.

"""


import itertools

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99, 'a', 'b']


# TODO
# print elements of `xpts` and `ypts` at once using `zip()`
# Now print ALL elements of `xpts` and `ypts` at once using `zip()`


headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
# TODO
# Make a dict from `headers` and `values` above


if __name__ == '__main__':
    pass
