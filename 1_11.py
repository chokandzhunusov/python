"""
************************************************************
**** 1.11. Naming a Slice
************************************************************


#########
# Problem
#########
# Your program has become an unreadable mess
# of hardcoded slice indices and you want to clean it up.


#########
# Solution
#########
# Name mysterious hardcoded indices.
"""

# Suppose you have some code that is pulling specific data fields out
# of a record string with fixed fields (e.g., from a flat file or similar format):

record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])

# TODO
# Clean the statements above by giving names to `slices`


if __name__ == '__main__':
    pass
