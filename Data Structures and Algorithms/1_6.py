'''
************************************************************
**** Mapping Keys to Multiple Values in a Dictionary Problem
************************************************************


#########
# Problem
#########
# You want to make a dictionary that maps keys to more than one value
# (a so-called “multidict”).

#########
# Solution
#########
# A dictionary is a mapping where each key is mapped to a single value.
# If you want to map keys to multiple values,
# you need to store the multiple values in another container such as a list or set.
'''

# For example, you might make dictionaries like this:

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}


from collections import defaultdict

# TODO
# Initialize an dictionary that stores `list` values
# Append items to it


# TODO
# Initialize an dictionary that stores `set` values
# Add items to it

if __name__ == '__main__':
    pass
