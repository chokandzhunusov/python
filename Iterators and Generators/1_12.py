"""
****************************************************
**** 4.12. Iterating on Items in Separate Containers
****************************************************

#########
# Problem
#########
# You need to perform the same operation on many objects,
# but the objects are contained in different containers,
# and you’d like to avoid nested loops without losing the readability of your code.

#########
# Solution
#########
# The itertools.chain() method can be used to simplify this task.
# It takes a list of iterables as input, and returns an iterator
# that effectively masks the fact that you’re really acting on multiple containers.
# This solution is much more elegant than using two separate loops.

# Inefficent
    for x in a + b: ...
# Better
    for x in chain(a, b): ...

"""


from itertools import chain


a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

# TODO
# print elements of a and b but at once using `chain()`
# Now print ALL elements of `xpts` and `ypts` at once using `zip()`


if __name__ == '__main__':
    pass
