"""
************************************************************
**** 1.10. Removing Duplicates from a Sequence while Maintaining Order
************************************************************


#########
# Problem
#########
# You want to eliminate the duplicate values in a sequence,
# but preserve the order of the remaining items.


#########
# Solution
#########
# If the values in the sequence are hashable,
# the problem can be easily solved using a set and a generator.
"""

# TODO
# Given a hashable sequence of items.
# Implement a function that will remove duplicates from it.


def dedupe_hashable(items):
    pass

# TODO
# Given an unhashable sequence of items.
# Implement a function that will remove duplicates from it.


a = [
    {'x': 1, 'y': 2},
    {'x': 1, 'y': 3},
    {'x': 1, 'y': 2},
    {'x': 2, 'y': 4}
]


def dedupe_unhashable(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    pass
