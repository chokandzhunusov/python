'''
*************************************************
**** Finding the Largest or Smallest N Items
*************************************************


#########
# Problem
#########
# You want to make a list of the largest or smallest N items in a collection.

#########
# Solution
#########
# The `heapq` module has two functions: nlargest() and nsmallest().
'''

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# TODO
# Print 3 largest ints of var `nums` above
# Print 3 smallest ints of var `nums` above


# Both functions also accept a key parameter that allows them to be used with more complicated data structures.
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# TODO
# Find 3 chapest shares from `portfolio` data above.    HINT: use `lambda`


if __name__ == '__main__':
    pass
