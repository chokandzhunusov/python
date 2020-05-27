"""
************************************************************
**** 1.18.  Mapping Names to Sequence Elements
************************************************************


#########
# Problem
#########
# You have code that accesses list or tuple elements by position,
# but this makes the code somewhat difficult to read at times.
# You’d also like to be less dependent on position in the structure,
# by accessing the elements by name.


#########
# Solution
#########
# `collections.namedtuple()` provides these benefits
"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

# TODO
# Create `namedtuple` called `Subscriber`, which takes 2 fields: `addr`, `joined`
# Create and instance of newly created `Subscriber`


# INFO
# References to positional elements often make the code a bit less expressive
# and more dependent on the structure of the records. e.g.

def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
        return total


Stock = namedtuple('Stock', ['name', 'shares', 'price'])

# TODO
# Finish function below, so that it involves above `Stock` instance to `compute_cost`


def compute_cost_nt(records):
    total = 0.0
    for rec in records:
        pass
    return

# INFO
# One possible use of a namedtuple is as a replacement for a dictionary,
# which requires more space to store.
# Thus, if you are building large data structures involving dictionaries,
# use of a namedtuple will be more efficient.
# However, be aware that unlike a dictionary, a namedtuple is immutable.


s = Stock('ACME', 100, 123.45)
# TODO
# Replace `shares` value to 75


# INFO
# If the goal is to define an efficient data structure
# where will be changing various instance attributes,
# using `namedtuple` is not best choice.
# Instead, consider defining a class using __slots__ instead

if __name__ == '__main__':
    pass
