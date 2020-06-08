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
# Write an `if/else` clause that determines `true/false` of `text1`
# and `text2` match using `re`


# TODO
# Precompile the regular expression pattern into a pattern object first
# DO the previous `TODO` with compiled version


text3 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# TODO
# `match` searches only starts with occurrence in the string
# but you need to FIND ALL matches in text, find them


# INFO
# When defining regular expressions, it is common to introduce `capture groups`
# by enclosing parts of the pattern in parentheses.


# TODO
# Compile `\d+/\d+/\d+` pattern with capture groups
# Print out `groups`(from 0, 3)
# Extract them to `month, day, year`
# Find all matches from `text3` using pattern with compiled groups
# Loop over them and print items in format: `month-day-year`


# TODO
# Loop over matches found using `findall`,
# but this time iteratively using `finditer()`


# INFO
# If you want an exact match,
# make sure the pattern includes the end-marker `$`


text4 = '12/23/2020awdaw'
# TODO
# Try to find exact match of date in `text4`


if __name__ == '__main__':
    pass
