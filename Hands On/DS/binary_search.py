##################################
#   Binary Search

"""
Best case  => O(1)
Worst case => O(logn)
"""
##################################


def binary_search_iter(low, high, items, key):
    """
    Iterative approach of BS
    :param low: lower bound of items
    :param high: upper bound of items
    :param items: ordered sequence of integers
    :param key: num to be searched in items
    :return: index at where found `key` or `-1`
    """
    while low <= high:
        mid = int((low+high)/2)
        if items[mid] == key:
            print(f'Item found at index: {mid}')
            return mid

        if key < items[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print(f'The number was not found.')
    return -1


def binary_search_recur(low, high, items, key):
    """
    Recursive approach of BS
    :param low: lower bound of items
    :param high: upper bound of items
    :param items: ordered sequence of integers
    :param key: num to be searched in items
    :return: index at where found `key` or `-1`
    """
    if low <= high:
        mid = int((low + high) / 2)
        if items[mid] == key:
            print(f'Item found at index: {mid}')
            return mid

        if key < items[mid]:
            return binary_search_recur(low, mid - 1, items, key)
        else:
            return binary_search_recur(mid + 1, high, items, key)
    print(f'The number was not found.')
    return -1


if __name__ == '__main__':
    items = [0, 1, 2, 3, 4, 5, 7]
    binary_search_iter(0, len(items)-1, items, 2)
    binary_search_recur(0, len(items)-1, items, 7)
