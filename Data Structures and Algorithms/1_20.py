"""
************************************************************
**** 1.20.  Combining Multiple Mappings into a Single Mapping
************************************************************


#########
# Problem
#########
# You have multiple dictionaries or mappings that you want to
# logically combine into a single mapping to perform certain operations,
# such as looking up values or checking for the existence of keys.
"""

from collections import ChainMap


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
# TODO
# Perform a lookup first by looking at `a` then at `b`. Use `chainmap()` to take it easy!
# Print x, y, z
# Waht is the `length`, `keys` and `values` of map created above
# Mutate `a` by changing its value `z=10`, `w=40` and remove `x`. Do not access `a` directly use map created earlier!
# Print `a` not map created above. And see changes
# Try to delete `y` from map. What it returns?


# TODO
# Merge `a` and `b` using `update()`
# NOTE: if any of the original dictionaries mutate,
# the changes don’t get reflected in the merged dictionary if you've used `update()`





if __name__ == '__main__':
    pass
