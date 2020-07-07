"""
************************************************************
**** 1.1.  Splitting Strings on Any of Multiple Delimiters
************************************************************


#########
# Problem
#########
# You need to split a string into fields,
# but the delimiters (and spacing around them)
# aren’t consistent throughout the string.


#########
# Solution
#########
# The `split()` method of string objects is really meant
# for very simple cases, and does not allow for multiple delimiters
# or account for possible whitespace around the delimiters.
# In cases when you need a bit more flexibility, use the `re.split()` method
"""

import re


line = 'asdf fjdk; afed, fjek,asdf, foo'

# TODO
# Split the variable `line` above by:
# semicolumn (`;`) comma (`,`)  and spaces (` `) using `re`
# space in regular expression => `\s`


# TODO
# Split the variable `line` into var `fields` but this time
# include the matched results
# HINT: Just add `|`


# TODO
# Use `list step` to solve following TODO's
# Extract `values` from `fields` you created above
# Extract `delimeters` from `fields` you created above(TRICKY
# when will try to recreate `line`)


# TODO
# Now recreate the var `line` from `values` and `delimeters`
# ''.join(v+d for v,d in zip(values, delimiters))

if __name__ == '__main__':
    pass

