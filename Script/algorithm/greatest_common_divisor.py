from basic_algorithm.utils import is_even


def greatest_common_divisor(num1: int, num2: int):
    if num1 < num2:
        num1, num2 = num2, num1

    if not num2:
        return num1

    if is_even(num1) and is_even(num2):
        return 2 * greatest_common_divisor(num1 >> 1, num2 >> 1)
    elif is_even(num1) and not is_even(num2):
        return greatest_common_divisor(num1 >> 1, num2)
    elif is_even(num2) and not is_even(num1):
        return greatest_common_divisor(num2 >> 1, num1)
    else:
        return greatest_common_divisor(num1 - num2, num2)


if __name__ == '__main__':
    assert greatest_common_divisor(3, 1) == 1
    assert greatest_common_divisor(42, 30) == 6
    assert greatest_common_divisor(77774396, 4396) == 28
