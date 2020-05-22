"""
************************************************************
**** 1.15. Grouping Records Together Based on a Field
************************************************************


#########
# Problem
#########
# You have a sequence of dictionaries or instances
# and you want to iterate over the data in groups
# based on the value of a particular field, such as `date`.


#########
# Solution
#########
# The `itertools.groupby()` function is particularly useful for grouping data together like this.
"""

from operator import itemgetter
from itertools import groupby
from collections import defaultdict


# Suppose you have the following list of dictionaries:
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# TODO
# Sort `rows` by date
# Iterate in groups

# TODO
# Group the data together by `date`s into a large data structure that allows random access
# Use `defaultdict()`


if __name__ == '__main__':
    pass
