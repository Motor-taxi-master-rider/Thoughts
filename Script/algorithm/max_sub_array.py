def max_sub_array(array):
    current_start = max_end = max_start = None
    max_sum = sum_current = 0
    for index, value in enumerate(array):
        if sum_current + value < 0:
            current_start = index + 1
            sum_current = 0
        else:
            sum_current = sum_current + value
        if sum_current > max_sum:
            max_start = current_start
            max_end = index
            max_sum = sum_current

    return max_sum, max_start, max_end


if __name__ == '__main__':
    test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_value, start, end = max_sub_array(test)
    assert test[start:end + 1] == [4, -1, 2, 1]
    assert max_value == 6

    test = [-2, 1, -3]
    max_value, start, end = max_sub_array(test)
    assert test[start:end + 1] == [1]
    assert max_value == 1

    test = [-2, -1, -3]
    max_value, start, end = max_sub_array(test)
    assert start is None and end is None
    assert max_value == 0