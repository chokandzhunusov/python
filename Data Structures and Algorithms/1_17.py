"""
************************************************************
**** 1.17.  Extracting a Subset of a Dictionary
************************************************************


#########
# Problem
#########
# You want to make a dictionary that is a subset of another dictionary.


#########
# Solution
#########
# This is easily accomplished using a dictionary comprehension.
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# TODO
# Make a `dict` of all `prices` above that value > 200 by using dictionary comprehension

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# Make a dictionary of tech stocks.

# Using `key, val for dict.items()` solutions(list comprehension)
# is almost 1.6 times faster than the access by key[val]

# And using tuple version `((key, val) for key, val in dict.items())`
# is at least twice slower that simple `key, val`

if __name__ == '__main__':
    pass
