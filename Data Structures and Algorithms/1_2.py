'''
**********************************************************
**** Unpacking Elements from Iterables of Arbitrary Length
**********************************************************
'''


#########
# Problem
#########
# You need to unpack N elements from an iterable, 
# but the iterable may be longer than N elements, 
# causing a “too many values to unpack” exception.


#########
# Solution
#########
# Python “star expressions” can be used to address this problem.
# For example, suppose you run a course and decide at the end of the semester that you’re going to drop the first and last homework grades, and only average the rest of them.  # noqa
# If there are only four assignments, maybe you simply unpack all four, but what if there are 24?   # noqa
# A star expres‐ sion makes it easy:

def drop_first_last(grades):
    # TODO
    # Return average of grades, except first and last
    pass


if __name__ == '__main__':
    grades = [5, 5, 3, 4, 5]
    avrg = drop_first_last(grades)
    print(f'The average of {grades} is: {avrg}')
