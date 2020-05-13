"""
************************************************************
**** 1.8. Calculating with Dictionaries Problem
************************************************************


#########
# Problem
#########
# You want to perform various calculations
# (e.g., minimum value, maximum value, sort‐ ing, etc.) on a dictionary of data.

#########
# Solution
#########
# In order to perform useful calculations on the dictionary contents,
# it is often useful to invert the keys and values of the dictionary using zip().
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# TODO
# Find the `min` of prices
# Find the `max` of prices
# Rank the data from lowest > highest

# When doing these calculations,
# be aware that zip() creates an iterator that can only be consumed once.

# TODO
# `zip` prices above and assign them to `var`
# Reproduce zip `err` by using it twice


if __name__ == '__main__':
    pass

