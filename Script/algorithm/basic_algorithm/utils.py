def is_even(num: int):
    return not num & 1


if __name__ == '__main__':
    assert is_even(2)
    assert not is_even(1)
