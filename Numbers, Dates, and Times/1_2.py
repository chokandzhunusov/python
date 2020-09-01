"""
************************************************************
**** 1.2. Performing Accurate Decimal Calculations
************************************************************


#########
# Problem
#########
# You need to perform accurate calculations with decimal numbers,
# and don’t want the small errors that naturally occur with floats.


#########
# Solution
#########
# A well-known issue with floating-point numbers is that they
# can’t accurately represent all base-10 decimals.
# Moreover, even simple mathematical calculations introduce small errors.

# If you want more accuracy (and are willing to give up some performance),
# you can use the decimal module
"""


from decimal import Decimal, localcontext


# TODO
# Compare 4.2 + 2.1 with 6.3


# TODO
# DO the same above, but this time using `Decimal` module


# INFO
# A major feature of decimal is that it allows you to control
# different aspects of calculations,
# including number of digits and rounding.
# To do this, you create a local context and change its settings.

# TODO
# Initialize 2 Decimal variables, use: 2.3 and 3.7.
# Try to cut its decimal value till 3 digits using `localcontext.prec`.


if __name__ == '__main__':
    pass
