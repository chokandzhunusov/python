'''
**********************************************************
**** Unpacking Elements from Iterables of Arbitrary Length
**********************************************************


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
'''

grades = [5, 5, 3, 4, 5]


def drop_first_last(grades):
    # TODO
    # Return average of grades, except first and last
    pass


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# TODO
# Unpack so that tel nums assigned to one var

# The starred variable can also be the first one in the list.
# For example, say you have a sequence of values representing your company’s sales figures for the last eight quarters.     # noqa
sales_record = [19, 32, 22, 29, 45, 66, 13, 41]
# TODO
# Find average of the first seven

# It is worth noting that the star syntax can be especially useful when iterating over a sequence of tuples of varying length.  # noqa
# For example, perhaps a sequence of tagged tuples:
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)

# TODO
# Iterate over records so that if/else statements will compare first item in tuple  # noqa

# Star unpacking can also be useful when combined with certain kinds of string processing operations, such as splitting.    # noqa
# For example:


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# TODO
# Unpack username and homedir

# Sometimes you might want to unpack values and throw them away.
# You can’t just specify a bare * when unpacking, but you could use a common throwaway variable name, such as _ or ign (ignored).   # noqa
# For example:
record = ('ACME', 50, 123.45, (12, 18, 2012))
# TODO
# Unpack to values name and year by ignoring others


items = [1, 10, 7, 4, 5, 9]
# TODO
# Split into head nad tail

# One could imagine writing functions that perform such splitting in order to carry out some kind of clever recursive algorithm.  # noqa
# TODO
# Write a recursive function so that it returns sum of given ints
# For example:


def sum(items):
    pass


if __name__ == '__main__':
    pass
