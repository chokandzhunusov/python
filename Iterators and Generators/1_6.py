"""
*******************************************************
**** 4.6. Defining Generator Functions with Extra State
*******************************************************

#########
# Problem
#########
# You would like to define a generator function,
# but it involves extra state that you would like to expose to the user somehow.

#########
# Solution
#########
# If you want a generator to expose extra state to the user,
# don’t forget that you can easily implement it as a class,
# putting the generator function code in the __iter__() method.

"""


from collections import deque


# TODO
# Complete following functions of the class
class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        # Code goes here
        # Create var called `history` and make it to keep 3 records max in queue

    def __iter__(self):
        # Code goes here
        # Iterate over lines and append them into history by enumerating
        # yield line
        pass

    def clear(self):
        self.history.clear()


if __name__ == '__main__':
    with open('./somefile.txt') as f:
        # Code goes here
        # Print history if word=python met in line
        pass
