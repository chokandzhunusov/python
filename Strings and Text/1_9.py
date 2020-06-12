"""
************************************************************
**** 1.9. Normalizing Unicode Text to a Standard Representation
************************************************************


#########
# Problem
#########
# You’re working with Unicode strings,
# but need to make sure that all of the strings have
# the same underlying representation.

#########
# Solution
#########
# Via examples
"""

import unicodedata


# In Unicode, certain characters can be represented by more than
# one valid sequence of code points.
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
# TODO
# Print them out and see the output
# Compare them(==)


# TODO
# Normalize `s1` and `s2` with 'NFC'(fully composed). And compare them(==)
# Normalize `s1` and `s2` with 'NFD'(fully decomposed). And compare them(==)


if __name__ == '__main__':
    pass
