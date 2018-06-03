import numpy as np


class Graph:
    UNVISITED = 0
    VISITED = 1

    def __init__(self, vertex_num: int):
        self._vertex_num = vertex_num
        self._edge_num = 0
        self._mark = [self.UNVISITED] * vertex_num
        self._matrix = np.zeros((vertex_num, vertex_num), dtype=np.float16)

    def n(self) -> int:
        return self._vertex_num

    def e(self) -> int:
        return self._edge_num

    def first(self, row: int) -> int:
        for col_index, value in enumerate(self._matrix[row]):
            if value != 0 and value != np.inf:
                return col_index
        return self._vertex_num

    def next(self, row: int, col: int) -> int:
        for col_index, value in enumerate(self._matrix[row][col + 1:], start=col + 1):
            if value != 0 and value != np.inf:
                return col_index
        return self._vertex_num

    def set_edge(self, row: int, col: int, weight: int):
        assert weight > 0 and row != col
        if self._matrix[row, col] == np.inf:
            self._edge_num += 1
        self._matrix[row, col] = weight

    def del_edge(self, row: int, col: int):
        assert row != col
        if self._matrix[row, col] != np.inf:
            self._edge_num -= 1
        self._matrix[row, col] = np.inf

    def is_edge(self, row: int, col: int) -> bool:
        assert row != col
        return not self._matrix[row, col] == np.inf

    def weight(self, row: int, col: int) -> int:
        return self._matrix[row, col]

    def get_mark(self, vertex_index: int) -> int:
        return self._mark[vertex_index]

    def set_mark(self, vertex_index: int, val: int):
        self._mark[vertex_index] = val

    def reset_mark(self):
        self._mark = [self.UNVISITED for _ in self._mark]
