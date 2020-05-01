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


with open('file_1_3.txt') as f:
    for line, previous_lines in search(f, 'python'):
        print(line, previous_lines)
        print('-'*20)


if __name__ == '__main__':
    pass
