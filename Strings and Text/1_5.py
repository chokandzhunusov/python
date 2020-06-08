"""
************************************************************
**** 1.5. Searching and Replacing Text
************************************************************


#########
# Problem
#########
# Search and replace a text pattern in a string.


#########
# Solution
#########
# For simple literal patterns, we use the `str.replace()` method.
# For more complicated patterns, we use the `sub()` functions/methods in the re module.
"""


import re
from calendar import month_abbr


text = 'yeah, but no, but yeah, but no, but yeah'
# TODO
# Replace all `yeah` wit `yep` using `replace()`


text2 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# TODO
# Replace dates(month/day/year) with => `year-month-day`


# TODO
# Specify a substitution callback function called `change_date`
# that converts month num to abbr using `month_abbr`


# TODO
# Use `subn()` method to know how many substitutions
# were made during replacement in `text2`


if __name__ == '__main__':
    pass
