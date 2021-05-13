"""
**********************************************
**** 3.15. Converting Strings into Datetimes
**********************************************


#########
# Problem
#########
# Your application receives temporal data in string format,
# but you want to convert those strings into datetime objects
# in order to perform nonstring operations on them.


#########
# Solution
#########
# Python’s standard datetime module is typically the easy solution for this.
# NOTE: that strftime() method involves many calculation
#       which involves system locale settings. So, if case is with dealing
#       with large of num date data better to write own function.
"""


from datetime import datetime


text = '2012-09-20'
# TODO
# convert above date into datetime object


z = datetime.now()
# TODO
# Make `z` look nice at output


# TODO
# Write a function that will a nearly 7 times faster than `strftime()`


if __name__ == '__main__':
    pass
