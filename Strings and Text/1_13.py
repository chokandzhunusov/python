"""
************************************************************
**** 1.13. Aligning Text Strings
************************************************************


#########
# Problem
#########
# You need to format text with some sort of alignment applied.


#########
# Solution
#########
# For basic alignment of strings, the `ljust()`, `rjust()`,
# and `center()` methods of strings can be used.
"""


text = 'Hello World'
# TODO
# Adjust `text` to left by 20 total width of  chars
# Adjust `text` to right by 20 total width of  chars
# Adjust `text` to center by 20 total width of  chars


# TODO
# Do the same thing done above with `format()` function


x = 1.2345
# TODO
# By  using the benefit of `format()` function,
# which is applicable to numbers. Center text by width of 20 chars.
# Cut float do hundredth.


if __name__ == '__main__':
    format(x, '=^20.2f')
