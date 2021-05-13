"""
************************************
**** 3.14. Finding the Date Range for the Current Month
************************************


#########
# Problem
#########
# You have some code that needs to loop over each date in the current month,
# and want an efficient way to calculate that date range.


#########
# Solution
#########
# Looping over the dates doesn’t require building a list of all the dates ahead of time.
# You can just calculate the starting and stopping date in the range,
# then use `datetime.timedelta` objects to increment the date as you go.
"""


import calendar

from datetime import datetime, date, timedelta

def get_month_range(start_date=None):
    if start_date is None:
        # Code goes here
        # Initialize start_date with first day of the month
        pass
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    # Code goes here
    # Define end_date use timedelta
    return (start_date, end_date)


def print_days_of_month():
    # Code goes here
    # Initialize `a_day` with day=1
    a_day = ''
    first_day, last_day = get_month_range()
    while first_day < last_day:
        print(first_day)
        first_day += a_day


def date_range(start, stop, step):
    # Code goes here
    # Create a while loop that will will yield start while start < stop with step=step
    pass


for d in date_range(datetime(2012, 9, 1), datetime(2012,10,1), timedelta(hours=6)):
    print(d)


if __name__ == '__main__':
    pass
