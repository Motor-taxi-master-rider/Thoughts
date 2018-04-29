import numpy as np


def random_list(lst):
    """randomize elements in O(n) time and in-place"""
    lst = np.array(lst)
    for i in reversed(range(len(lst))):
        random_index = np.floor(np.random.random() * (i + 1)).astype(np.int16)
        lst[i], lst[random_index] = lst[random_index], lst[i]

    return lst


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    print(random_list(lst))
