"""
************************************************************
**** 1.12. Determining the Most Frequently Occurring Items in a Sequence
************************************************************


#########
# Problem
#########
# You have a sequence of items,
# and you’d like to determine the most frequently occurring items in the sequence.


#########
# Solution
#########
# The `collections.Counter` class is designed for just such a problem.
# It even comes with a handy `most_common()` method that will give you the answer.
# As input, Counter objects can be fed any sequence of hashable input items.
"""

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look',
    'into', 'my', 'eyes', "you're", 'under'
]

more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

# TODO
# Filter the `words` var above, so that it counts repeated words
# Print the first(top) three most occurred words in `words` var
# NOTE: the above two TODO'S return diff data structures


# TODO
# Add `more_words` to words using method not loop

# TODO
# Combine `words` and  `more_words`
# Subtract `more_words` from  `words`


if __name__ == '__main__':
    pass
