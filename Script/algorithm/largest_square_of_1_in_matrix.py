import numpy as np


def largest_square_of_1_in_matrix(matrix):
    """find largest square size which is consisted of 1 in given matrix"""
    largest_square_size = 1 if 1 in matrix else 0
    square_matrix = np.array(matrix)
    for i in reversed(range(square_matrix.shape[0] - 1)):
        for j in reversed(range(square_matrix.shape[1] - 1)):
            if matrix[i, j] == 1:
                right, corner, down = square_matrix[i + 1, j], square_matrix[i + 1, j + 1], square_matrix[i, j + 1]
                if right and down and corner:
                    square_size = 1 + corner
                    square_matrix[i, j] = square_size
                    largest_square_size = max(square_size, largest_square_size)
    return largest_square_size


if __name__ == '__main__':
    test = np.array([[1, 1, 0, 1, 0],
                     [0, 1, 1, 1, 0],
                     [1, 1, 1, 1, 0],
                     [0, 1, 1, 1, 1]])
    assert largest_square_of_1_in_matrix(test) == 3

    test = np.array([[0, 1], [1, 1]])
    assert largest_square_of_1_in_matrix(test) == 1

    test = np.array([[1, 1], [1, 1]])
    assert largest_square_of_1_in_matrix(test) == 2

    test = np.array([[1, 0], [1, 1]])
    assert largest_square_of_1_in_matrix(test) == 1
