"""
**********************************************
**** 3.16. Manipulating Dates Involving Time Zones
**********************************************


#########
# Problem
#########
# You had a conference call scheduled for December 21, 2012, at 9:30 a.m. in Chicago.
# At what local time did your friend in Bangalore, India, have to show up to attend?


#########
# Solution
#########
# For almost any problem involving time zones,
# you should use the pytz module.
# This package provides the Olson time zone database,
# which is the de facto standard for time zone information
# found in many languages and operating systems.
"""

from datetime import datetime
from pytz import timezone


# TODO
# Initialize datetime object for date mentioned in problem
# Use `US/Central` to initialize timezone
# Localize datetime
# Now convert that localized datetime to `Asia/Bishkek` time


if __name__ == '__main__':
    pass
