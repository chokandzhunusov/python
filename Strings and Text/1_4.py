"""
************************************************************
**** 1.4. Matching and Searching for Text Patterns
************************************************************


#########
# Problem
#########
# We want to match or search text for a specific pattern.


#########
# Solution
#########
# If the text you’re trying to match is a simple literal,
# we can often just use the basic string methods,
# such as `str.find()`, `str.endswith()`, `str.startswith()`.
# For more complicated matching, use regular expressions and the `re` module.
"""

import re


text = 'yeah, but no, but yeah, but no, but yeah'

# TODO
# Search for the location of the first occurrence of word `no` in `text` above


# INFO
# \d+ means match one or more digits

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
# TODO
# Write an `if/else` clause that determines `true/false` of match using `re`

if __name__ == '__main__':
    pass
