"""
********************************************
**** 5.8. Iterating Over Fixed-Sized Records
********************************************

#########
# Problem
#########
#   Instead of iterating over a file by lines,
    you want to iterate over a collection of fixed-sized records or chunks.

#########
# Solution
#########
#   Use the iter() function and functools.partial()
    partial takes the file and the size of chunk

NOTE: Apllicable only to binary data!
      The sentinel of b'' is what gets returned when a file
      is read but the end of file has been reached.

"""


from functools import partial

RECORD_SIZE = 10


# TODO
#   Open some file with iter() in binary mode by passing
#   to it partial() amount of data(RECORD_SIZE) and print
#   chunks of data. Treat only in binary.


if __name__ == '__main__':
    pass
