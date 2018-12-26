from collections import namedtuple
import numpy as np

Cost = namedtuple('Cost', ['insert', 'delete', 'replace'])


def lowest_string_edit_cost(source: str, target: str, costs: Cost):
    cost_matrix = np.asmatrix(np.zeros(shape=(len(source) + 1, len(target) + 1)))


if __name__ == '__main__':
    assert lowest_string_edit_cost('abc', 'adc', Cost(insert=5, delete=3, replace=2)) == 2
