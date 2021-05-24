"""
******************************
**** 4.5. Iterating in Reverse
******************************

#########
# Problem
#########
# You want to iterate in reverse over a sequence.

#########
# Solution
#########
# Use the built-in reversed() function.

"""


# TODO
# Complete following functions of the class
class Countdown:
    def __init__(self, point):
        self.point = point

    def __iter__(self):
        # Code goes here
        pass

    def __reversed__(self):
        # Code goes here
        pass


if __name__ == '__main__':
    c = Countdown(4)
    for i in c:
        print(i)

    for j in reversed(c):
        print(j)
    pass
