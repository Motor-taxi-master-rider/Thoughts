from functools import lru_cache
from collections import namedtuple

Item = namedtuple('Item', ['weight', 'value'])

def knapsack(items, package_size):
    @lru_cache()
    def helper(n, capacity):
        if n < 0 or capacity == 0:
            return 0
        if items[n].weight > capacity:
            return helper(n-1, capacity)
        return max(helper(n-1, capacity), items[n].value + helper(n-1, capacity - items[n].weight))

    return helper(len(items) - 1, package_size)


if __name__ == '__main__':
    items = [Item(1,5),Item(2,3),Item(4,5),Item(3,3),Item(5,2)]
    print(knapsack(items, 3))
