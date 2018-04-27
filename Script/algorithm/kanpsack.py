from functools import lru_cache
from operator import attrgetter
from collections import namedtuple

Item = namedtuple('Item', ['weight', 'value'])
Result = namedtuple('Result', ['total_value', 'picked_items'])


def knapsack(items, package_size):
    @lru_cache()
    def helper(n, capacity, package):
        if n < 0 or capacity == 0:
            return Result(total_value=0, picked_items=package)
        if items[n].weight > capacity:
            return helper(n - 1, capacity, package)
        return max(helper(n - 1, capacity, package),  # case not choose current item
                   Result(total_value=helper(n - 1, capacity - items[n].weight, package).total_value + items[n].value,
                          picked_items=helper(n - 1, capacity - items[n].weight, package).picked_items + (items[n],)),
                   key=attrgetter('total_value'))

    return helper(len(items) - 1, package_size, tuple())


if __name__ == '__main__':
    def chosen_items(*index):
        return tuple(items[index] for index in index)


    items = [Item(1, 5), Item(2, 3),
             Item(4, 5), Item(2, 3), Item(5, 2)]
    capacity = 10
    assert knapsack(items, capacity) == Result(total_value=16, picked_items=chosen_items(0, 1, 2, 3))

    items = [Item(77, 92), Item(22, 22),
             Item(29, 87), Item(50, 46), Item(99, 90)]
    capacity = 100
    assert knapsack(items, capacity) == Result(total_value=133, picked_items=chosen_items(2, 3))

    items = [Item(79, 83), Item(58, 14), Item(86, 54),
             Item(11, 79), Item(28, 72), Item(62, 52),
             Item(15, 48), Item(68, 62)]
    capacity = 200
    assert knapsack(items, capacity) == Result(total_value=334, picked_items=chosen_items(0, 3, 4, 5, 6))
