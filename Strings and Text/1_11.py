"""
************************************************************
**** 1.11. Stripping Unwanted Characters from Strings
************************************************************


#########
# Problem
#########
# You want to strip unwanted characters,
# such as whitespace, from the beginning,
# end, or middle of a text string.


#########
# Solution
#########
# The strip() method can be used to strip characters
# from the beginning or end of a string.
# `lstrip()` and `rstrip()` perform stripping from
# the left or right side, respectively.
# By default, these methods strip whitespace,
# but other characters can be given.
"""


import re


s = '    hello world \n'
# TODO
# Remove whitespaces at the beginning and end from `s`
# Now remove from left
# Remove from right


t = '-----hello====='
# TODO
# Remove `-` chars from `t`
# Remove both `-` and `=` chars from `t`


k = ' hello          world \n'
# TODO
# Try to remove all whitespaces from `k` with `strip()`
# Now use `replace()`
# Now user regular expression


if __name__ == '__main__':
    pass
