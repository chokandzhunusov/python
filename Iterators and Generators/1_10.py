"""
*************************************************************
**** 4.10. Iterating Over the Index-Value Pairs of a Sequence
*************************************************************

#########
# Problem
#########
# You want to iterate over a sequence, but would like to keep track
# of which element of the sequence is currently being processed.

#########
# Solution
#########
# The built-in enumerate() function handles this quite nicely.

"""


import itertools


items = ['a', 'b', 'c']
items_2 = [0, 1, 2, 3]
# TODO
# print (index, val) of items at once


# TODO
# Use itertools.combinations() to produce a sequence of combinations
# of items.

if __name__ == '__main__':
    for i, val in enumerate(items_2):
        print(f'{i}: {val}')
    pass
