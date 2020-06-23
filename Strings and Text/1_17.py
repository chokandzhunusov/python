"""
************************************************************
**** 1.17. Handling HTML and XML Entities in Text
************************************************************


#########
# Problem
#########
# You want to replace HTML or XML entities such as `&entity;`
# or `&#code;` with their corresponding text.
# Alternatively, you need to produce text,
# but escape certain characters (e.g., <, >, or &).


#########
# Solution
#########
# If you are producing text, replacing special characters such as `<` or `>`
# is relatively easy if you use the `html.escape()` function.
"""


import html


s = 'Elements are written as "<tag>text</tag>".'
# TODO
# Try to print `s` with `html.escape()`
# Now disable escaping of quotes

# INFO
# Basically libs should already deal with many cases on HTML/XML parsing.


if __name__ == '__main__':
    pass
