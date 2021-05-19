"""
**********************************************
**** 4.2. Delegating Iteration
**********************************************


#########
# Problem
#########
# You have built a custom container object that internally holds
# a list, tuple, or some other iterable.
# You would like to make iteration work with your new container.


#########
# Solution
#########
# Typically, all you need to do is define an __iter__() method
# that delegates iteration to the internally held container.
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8]


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


if __name__ == '__main__':
    # TODO
    # Create 3 Node objects(root, ch1, ch2)
    # Add ch1, ch2 to root
    # Loop over root to see its children
    pass
