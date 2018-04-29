from functools import lru_cache


def find_set_number_of_sum_n(array, summary):
    """find all sub set in a list which summary equal to given number"""

    @lru_cache()
    def helper(n, summary, result):
        nonlocal fulfil_sets, array
        if summary == 0:
            fulfil_sets.append(result)
            return
        if n < 0 or summary < 0:
            return
        helper(n - 1, summary, result)
        helper(n - 1, summary - array[n], (array[n],) + result)

    fulfil_sets = []
    helper(len(lst) - 1, summary, tuple())
    return fulfil_sets


if __name__ == '__main__':
    lst = [2, 4, 6, 10]
    assert find_set_number_of_sum_n(lst, 16) == [(2, 4, 10), (6, 10)]

    lst = [2, 4, 6, 10]
    assert find_set_number_of_sum_n(lst, 17) == []

    lst = [1, 1, 2, 3, 5, 8, 13]
    assert find_set_number_of_sum_n(lst, 13) == [(1, 1, 3, 8), (2, 3, 8), (5, 8), (13,)]
