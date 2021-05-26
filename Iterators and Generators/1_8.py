"""
************************************************
**** 4.8. Skipping the First Part of an Iterable
************************************************

#########
# Problem
#########
# You want to iterate over items in an iterable,
# but the first few items aren’t of interest and you just want to discard them.

#########
# Solution
#########
# The itertools module has a few functions that can be used to address this task.
# The first is the itertools.dropwhile() function.
# To use it, you supply a function and an iterable.
# The returned iterator discards the first items in the sequence as
# long as the supplied function returns True.

"""


import itertools


# TODO
# Read file ./somefile and loop ove its lines.
# Using dropwhile wich takes 2 args lambda line:
# ignore lines which starts with `#`


items = ['a', 'b', 'c', 1, 4, 10, 15]
# TODO
# print elements of items by ignoring chars using islice method
# NOTE:
# In this example, the last None argument to islice() is required
# to indicate that you want everything beyond the first three items
# as opposed to only the first three items.

if __name__ == '__main__':
    pass
