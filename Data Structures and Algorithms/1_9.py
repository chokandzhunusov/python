"""
************************************************************
**** 1.9. Finding Commonalities in Two Dictionaries Problem
************************************************************


#########
# Problem
#########
# You have two dictionaries and want to find out what they might have in common (same keys, same values, etc.).


#########
# Solution
#########
# To find out what the two dictionaries have in common,
# simply perform common set operations using the keys() or items() methods.
"""

# Consider two dictionaries:
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# TODO
# Find common keys of two dicts above
# Find keys in `a` that are not in `b`
# Find common (key, value) pairs of `a` and `b`
# Make a new dictionary(by using dict comprehension) with certain keys(z, w) removed from dict `a`


if __name__ == '__main__':
    pass
