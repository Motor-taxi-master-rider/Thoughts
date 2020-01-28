from numpy import array


def pat(input: str) -> int:
    """ PAT B1040 """
    left_p = array([0] * len(input))
    right_t = array([0] * len(input))

    for i in range(len(input) - 1):
        if input[i] == 'P':
            left_p[i + 1] = left_p[i] + 1
        else:
            left_p[i + 1] = left_p[i]
    for j in range(len(input) - 1, 0, -1):
        if input[j] == 'T':
            right_t[j - 1] = right_t[j] + 1
        else:
            right_t[j - 1] = right_t[j]

    result = 0
    for index, character in enumerate(input):
        if character == 'A':
            result = left_p[index] * right_t[index]

    return result


if __name__ == '__main__':
    assert pat('APPAPT') == 2
