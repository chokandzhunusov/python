"""
***************************************
**** 4.14. Flattening a Nested Sequence
***************************************

#########
# Problem
#########
# You have a nested sequence that you want to flatten into a single list of values.

#########
# Solution
#########
# This is easily solved by writing a recursive generator function involving a yield from statement.

# TODO
#   - Write a function that will take an nested items of list dt, loop, if it
      is Iterable that it makes yield by recursive call of that inner items
      Else just yields item.
      Note the usage of `yields from` which is used for clean code
      and advanced programming.

    - Try to pass second arg `ignore_types` that will handle not to treat
      string and bytes as Iterable and apply it in conditional statement.

    - Above you used generators that call other generators as subroutines.
      Try to change it to `for loop`.
"""

from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


def flatten_strategy_2(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x


if __name__ == '__main__':
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    items2 = ['Dave', 'Paula', ['Thomas', 'Lewis']]

    for x in flatten(items):
        print(x)

    for y in flatten(items2):
        print(y)
