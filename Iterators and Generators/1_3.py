"""
**********************************************************
**** 4.3. Creating New Iteration Patterns with Generators
**********************************************************


#########
# Problem
#########
# You want to implement a custom iteration pattern that’s different than
# the usual built- in functions (e.g., range(), reversed(), etc.).



#########
# Solution
#########
# If you want to implement a new kind of iteration pattern,
# define it using a generator function.

"""

nums = [1, 2, 3, 4, 5, 6, 7, 8]

# NOTE: The mere presence of the yield statement in a function turns it into a generator.
# NOTE: Unlike a normal function, a generator only runs in response to iteration.
#       Otherwise you get object as you see.

# TODO
# Write a generator function that takes:
# `start`, `stop`, `step/increment` args and yields num at each step
# Note that in order to use that function you have to iterate using
# `for loop` or some function that consumes iterable(eg: sum, max...)


if __name__ == '__main__':
    pass
