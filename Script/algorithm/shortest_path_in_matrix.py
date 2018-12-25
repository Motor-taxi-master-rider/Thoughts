import numpy as np


def shortest_path_in_matrix(matrix: np.matrix):
    """矩阵的最小路径和
    给定一个矩阵m，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来就是
    路径和，返回所有的路径中最小的路径和。
    """
    distance_matrix = matrix.copy()
    row_max, col_max = matrix.shape

    for c in range(1, col_max):
        distance_matrix[0, c] = matrix[0, c] + matrix[0, c - 1]
    for r in range(1, row_max):
        distance_matrix[r, 0] = matrix[r, 0] + matrix[r - 1, 0]

    for col in range(1, col_max):
        for row in range(1, row_max):
            distance_matrix[row, col] = min(distance_matrix[row - 1, col], distance_matrix[row, col - 1]) \
                                        + matrix[row, col]
    return distance_matrix[-1, -1]


def shortest_path_in_matrix_less_space(matrix: np.matrix):
    """
    《程序员代码面试指南》P189
    """
    row, col = matrix.shape
    if row < col:
        matrix = matrix.T
        row, col = col, row

    distance_row = matrix[0, :].A1  # length = min(row, col)

    # Initial first row
    for c in range(1, col):
        distance_row[c] = distance_row[c - 1] + distance_row[c]

    for r in range(1, row):
        distance_row[0] = matrix[r, 0] + distance_row[0]
        for c in range(1, col):
            distance_row[c] = min(distance_row[c - 1], distance_row[c]) + matrix[r, c]

    return distance_row[-1]


if __name__ == '__main__':
    path_matrix = np.matrix([[1, 3, 5, 9, 5],
                             [8, 1, 3, 4, 6],
                             [5, 0, 6, 1, 7],
                             [8, 8, 4, 0, 0]])
    assert shortest_path_in_matrix(path_matrix) == 12
    assert shortest_path_in_matrix_less_space(path_matrix) == 12
