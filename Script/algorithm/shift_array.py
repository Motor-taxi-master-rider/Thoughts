from itertools import chain


def shift_array(vector: list, right_shift: int):
    right_shift %= len(vector)
    return list(reversed(list(chain.from_iterable([reversed(vector[:-right_shift]), reversed(vector[-right_shift:])]))))


if __name__ == '__main__':
    assert shift_array([1, 2, 3, 4, 5, 6], 2) == [5, 6, 1, 2, 3, 4]
    assert shift_array([1, 2, 3, 4, 5, 6], 8) == [5, 6, 1, 2, 3, 4]
