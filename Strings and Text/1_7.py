"""
************************************************************
**** 1.7. Specifying a Regular Expression for the Shortest Match
************************************************************


#########
# Problem
#########
# You’re trying to match a text pattern using regular expressions,
# but it is identifying the longest possible matches of a pattern.
# Instead, you would like to change it to find the shortest possible match.


#########
# Solution
#########
# Via examples
"""

import re


# This problem often arises in patterns that try to match text
# enclosed inside a pair of starting and ending delimiters
# (e.g., a quoted string).


text1 = 'Computer says "no."'
# TODO
# Compile a pattern that will search `string` within the `double quotes`
# inside of `text`
# Find all `pattern` matches in `text1`


text2 = 'Computer says "no." Phone says "yes."'
# TODO
# Try to find all `pattern` matches in `text2`
# Now you see that prev `todo` is GREEDY, fix it


if __name__ == '__main__':
    pass
