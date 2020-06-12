"""
************************************************************
**** 1.8. Writing a Regular Expression for Multiline Patterns
************************************************************


#########
# Problem
#########
# You’re trying to match a block of text using a regular expression,
# but you need the match to span multiple lines.

#########
# Solution
#########
# Via examples
"""

import re


# This problem typically arises in patterns that use
# the dot (.) to match any character but forget to account
# for the fact that it doesn’t match newlines.


text1 = '/* this is a comment */'
# TODO
# Compile a pattern that will search `string` with
# infinite left and right bounds inside of `text`
# Find all `pattern` matches in `text1`


text2 = '''/* this is a
        multiline comment */
        '''
# TODO
# Change `pattern` to be able search multiline by
# adding `(?:.|\n)` instead of dot(.)
# Try to find all `pattern` matches in `text2`


# TODO
# Try to find all matches in `text2` using simpler
# version of searching `multiline` by adding re.DOTALL while compiling

if __name__ == '__main__':
    pass
