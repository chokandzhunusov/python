"""
************************************************************
**** 1.3. Matching Strings Using Shell Wildcard Patterns
************************************************************


#########
# Problem
#########
# You want to match text using the same wildcard patterns as are
# commonly used when working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc.)


#########
# Solution
#########
# The fnmatch module provides two functions—fnmatch()
# and fnmatchcase()—that can be used to perform such matching.
"""


from fnmatch import fnmatch, fnmatchcase


# TODO
# Try to find `.py` matches in current dir with `fnmatch`


addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
# TODO
# Extract the matches from `addresses` above that matches `ST`


if __name__ == '__main__':
    pass
