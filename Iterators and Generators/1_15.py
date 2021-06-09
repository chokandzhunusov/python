"""
*****************************************************************
**** 4.15. Iterating in Sorted Order Over Merged Sorted Iterables
*****************************************************************

#########
# Problem
#########
# You have a collection of sorted sequences and you want to iterate
  over a sorted sequence of them all merged together.

#########
# Solution
#########
# The `heapq.merge()` function does exactly what you want.

# TODO
   - Given two sequence of elements a=[1, 3] and b=[2, 4]. Merge them but in sorted order
   - Given 2 files with sorted elements. Open them in read mode and Merge them by keeping order.
     Write them into 3rd file.
"""


import heapq


a = [1, 3, 5, 7]
b = [2, 4, 6, 8]


if __name__ == '__main__':
    pass

