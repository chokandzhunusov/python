##################################
#   Linear Search
##################################

"""
Best case  => O(1)
Worst case => O(n)
Average case => O(n)     (1+2+3+...+n)/n
                         (n(n+1)/2)/n
                         (n+1)/2
"""


def linear_search(items, key):
    """
    Used `move to head` approach to optimize LS
    :param items: list of items
    :param key: item to be searched
    :return: index at which found `key`
    """
    for index, item in enumerate(items):
        if item == key:
            temp = items[0]
            items[index] = temp
            items[0] = key
            print(f'Found key at index: {index}, and moved it to first position: {items}')
            return index


if __name__ == '__main__':
    linear_search(['a', 'b', 'c', 'd'], 'c')
