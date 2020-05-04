'''
*************************************************
**** Implementing a Priority Queue
*************************************************


#########
# Problem
#########
# You want to implement a queue that sorts items by a given priority
# and always returns the item with the highest priority on each pop operation.

#########
# Solution
#########
# The following class uses the heapq module to implement a simple priority queue.
'''

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = [] self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item)) self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# TODO
# Create an `Item` class which initially takes a name as param
# and should return object representation


# TODO
# Create an instance of `PriorityQueue` class above
# Push to it 4 'Item' objects
