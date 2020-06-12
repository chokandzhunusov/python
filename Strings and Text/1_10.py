"""
************************************************************
**** 1.10. Working with Unicode Characters in Regular Expressions
************************************************************


#########
# Problem
#########
# You are using regular expressions to process text,
# but are concerned about the handling of Unicode characters.

#########
# Solution
#########
# By default, the re module is already programmed with
# rudimentary knowledge of certain Unicode character classes.

# If you’re going to do it seriously,
# you should consider installing the third-party regex library,
# which provides full support for Unicode case folding,
# as well as a variety of other interesting features,
# including approximate matching.
"""


import re

# INFO
# `\d` already matches any unicode digit character


if __name__ == '__main__':
    pass
