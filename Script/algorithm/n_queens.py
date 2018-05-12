import copy


def n_queens_backtrack(n):
    array = []
    result = []

    def place_queen(col):
        nonlocal n, array
        if col == n:
            return True
        for row in range(n):
            array.append((row, col))
            if is_safe(row, col) and place_queen(col + 1):
                result.append(copy.copy(array))
            array.pop()
        return False

    def is_safe(row, col):
        for r, c in array[:-1]:
            if r == row:
                return False
            if abs(r - row) == abs(c - col):
                return False
        return True

    place_queen(0)
    return result


def n_queens_enumerate(n):
    array = [1] * n
    result = []

    def place_queen(array, col):
        nonlocal n, result
        if col == n:
            result.append(copy.copy(array))
            return
        for row in range(n):
            array[col] = row
            flag = True
            for c, r in enumerate(array[:col]):
                if r == row or abs(r - row) == abs(c - col):
                    flag = False
                    break
            if flag:
                place_queen(array, col + 1)

    place_queen(array, 0)
    return result


if __name__ == '__main__':
    assert len(n_queens_backtrack(8)) == 92
    assert len(n_queens_enumerate(8)) == 92
