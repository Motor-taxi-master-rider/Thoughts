from collections import namedtuple
import numpy as np

Cost = namedtuple('Cost', ['insert', 'delete', 'replace'])


def lowest_string_edit_cost(source: str, target: str, costs: Cost):
    """
    《程序员代码面试指南》P218
    :param source: 原字符串
    :param target: 目标字符串
    :param costs: 各种操作的代价
    :return: 将原字符串编辑成目标字符串的最小编辑代价
    """
    max_row, max_col = len(source) + 1, len(target) + 1
    cost_matrix = np.asmatrix(np.zeros(shape=(max_row, max_col)))
    # 第一位储存‘’（空字符串）编辑代价
    cost_matrix[0, :] = np.arange(max_col) * costs.insert
    cost_matrix[:, 0] = np.arange(max_row).reshape(max_row, 1) * costs.delete

    for col in range(1, max_col):
        for row in range(1, max_row):
            delete_then_edit = costs.delete + cost_matrix[row - 1, col]
            edit_then_add = cost_matrix[row, col - 1] + costs.insert
            replace_last = cost_matrix[row - 1, col - 1] + costs.replace
            if source[row - 1] == target[col - 1]:
                replace_last = replace_last - costs.replace

            cost_matrix[row, col] = min(delete_then_edit, edit_then_add, replace_last)

    return cost_matrix[-1, -1]


def lowest_string_edit_cost_less_space(source: str, target: str, costs: Cost):
    """
    《程序员代码面试指南》P219
    """
    if len(source) < len(target):
        costs.insert, costs.delete = costs.delete, costs.insert
        source, target = target, source

    max_row, max_col = len(source) + 1, len(target) + 1

    cost_row = np.arange(max_col + 1) * costs.insert

    for row in range(1, max_row):
        # 由于更新会覆盖数据，最后一位储存对角线编辑代价
        cost_row[-1] = cost_row[0]
        cost_row[0] = row * costs.delete
        for col in range(1, max_col):
            delete_then_edit = costs.delete + cost_row[col]
            edit_then_add = cost_row[col - 1] + costs.insert
            replace_last = cost_row[-1] + costs.replace
            if source[row - 1] == target[col - 1]:
                replace_last = replace_last - costs.replace

            cost_row[-1] = cost_row[col]
            cost_row[col] = min(delete_then_edit, edit_then_add, replace_last)

    return cost_row[-2]


if __name__ == '__main__':
    source, target, costs = 'abc', 'adc', Cost(insert=5, delete=3, replace=2)
    assert lowest_string_edit_cost(source, target, costs) == 2
    assert lowest_string_edit_cost_less_space(source, target, costs) == 2

    source, target, costs = 'abc', 'adc', Cost(insert=5, delete=3, replace=100)
    assert lowest_string_edit_cost(source, target, costs) == 8
    assert lowest_string_edit_cost_less_space(source, target, costs) == 8

    source, target, costs = 'abc', 'abc', Cost(insert=5, delete=3, replace=2)
    assert lowest_string_edit_cost(source, target, costs) == 0
    assert lowest_string_edit_cost_less_space(source, target, costs) == 0

    source, target, costs = 'ab12cd3', 'abcdf', Cost(insert=5, delete=3, replace=2)
    assert lowest_string_edit_cost(source, target, costs) == 8
    assert lowest_string_edit_cost_less_space(source, target, costs) == 8
