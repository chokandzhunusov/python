'''
*************************************************
**** Keeping the Last N Items
*************************************************


#########
# Problem
#########
# You want to keep a limited history of the last few items seen during iteration
# or during some other kind of processing.


#########
# Solution
#########
# Keeping a limited history is a perfect use for a `collections.deque`
'''

# For example, the following code performs a simple text match on a sequence of lines   # noqa
# and yields the matching line along with the previous N lines of context when found:   # noqa
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# TODO
# Open a file `file_1_3.txt`.
# Loop over each line
# print current line and prev lines


# When writing code to search for items,
# it is common to use a generator function involving `yield`.
# This decouples the process of searching from the code that uses the results

q = deque()
# TODO
# Add item to `q`
# Add item to the begginning of `q`
# Remove item to `q`
# Remove item to the begginning of `q`


# Adding or popping items from either end of a queue has O(1) complexity.
# This is unlike a list where inserting or removing items from the front of the list is O(N).   # noqa


if __name__ == '__main__':
    pass
