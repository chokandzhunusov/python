"""
********************************************
**** 4.4. Implementing the Iterator Protocol
********************************************


#########
# Problem
#########
# You are building custom objects on which you would like to support iteration,
# but would like an easy way to implement the iterator protocol.



#########
# Solution
#########
# Easiest way to implement iteration on an object is to use a generator function.
# Perhaps you want to implement an iterator that traverses nodes in a depth-first pattern.

"""


# TODO
# Complete following functions of the class
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        # Code goes here
        # return `value` that belongs to obj
        pass

    def add_child(self, node):
        # Code goes here
        # Add `node` to _children of obj
        pass

    def __iter__(self):
        # Code goes here
        # Make _children of obj iterable
        pass

    def depth_first(self):
        """
        - It first yields itself
        - Then iterates over each child yielding the items produced by the child’s depth_first() method (using yield from).
        """
        # Code goes here
        # Implement what described in docstrings
        pass


if __name__ == '__main__':
    root = Node(0)
    ch1 = Node(1)
    ch2 = Node(2)
    root.add_child(ch1)
    root.add_child(ch2)
    ch1.add_child(Node(3))
    ch1.add_child(Node(4))
    ch2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)
    pass
