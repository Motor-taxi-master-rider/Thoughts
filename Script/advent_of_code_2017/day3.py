import numpy as np


def solution(num):
    def cal_edge(num):
        return np.ceil(np.sqrt(num))

    def cal_center_diff(edge, num):
        mid_distance = num // 2
        upper_bound = edge ** 2
        diff = upper_bound - num
        edge_number = diff // mid_distance
        edge_mid = upper_bound - mid_distance - (edge - 1) * edge_number
        return num - edge_mid + edge // 2

    return cal_center_diff(cal_edge(num), num)


print(solution(265149))
