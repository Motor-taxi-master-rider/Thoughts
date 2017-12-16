import numpy as np


def solution(num):
    def cal_edge(num):
        return np.ceil(np.sqrt(num))

    def cal_layer(num):
        return num // 2

    def cal_mid_diff(edge, num):
        dct = {}
        diff = edge ** 2 - num
        np.floor(edge / 2)
        return dct.get(num, -1)


print(solution(438))
