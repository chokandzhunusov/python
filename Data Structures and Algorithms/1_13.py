"""
************************************************************
**** 1.13. Sorting a List of Dictionaries by a Common Key
************************************************************


#########
# Problem
#########
# You have a list of dictionaries and you would like to
# sort the entries according to one or more of the dictionary values.


#########
# Solution
#########
# Sorting this type of structure is easy using the `operator` module’s `itemgetter` function.
"""

from operator import itemgetter

# You’ve queried a database table to get a listing of the members on your website,
# and you receive the following data structure in return

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# TODO
# Filter the `rows` by `fname` and output in alphabetical order
# Filter the `rows` by `uid` and output from lowest too highest
# Filter the `rows` by `fname` and the `lname`. Then output in alphabetical order


if __name__ == '__main__':
    pass
