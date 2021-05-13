"""
************************************
**** 3.12. Converting Days to Seconds, and Other Basic Time Conversions
************************************


#########
# Problem
#########
# You have code that needs to perform simple time conversions,
# like days to seconds, hours to minutes, and so on.


#########
# Solution
#########
# To perform conversions and arithmetic involving
# different units of time, use the `datetime` module.

# For most basic date and time manipulation problems,
# the `datetime` module will suffice.
# If you need to perform more complex date manipulations,
# such as dealing with time zones, fuzzy time ranges,
# calculating the dates of holidays, and so forth, look at the `dateutil` module.
"""


from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta


# TODO
# Initialize time `a` and `b` using `timedelta` method
# Add them.
# Print it's days, hours and minutes.


# TODO
# Create a specific date and time called `x`.
# Add 10 hours to it using `timedelta()` method


# TODO
# Add 2 months to `x` using `relativedelta()` method
# Create 2 datetimes and try to find their diff `relativedelta()`


if __name__ == '__main__':
    pass
