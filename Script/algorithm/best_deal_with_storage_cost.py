"""
某商品在连续的K天内价格记录在prices数组中。经销商在某天（设为i）决定购入某商品，
将他们存入仓库。并在另外一天（设为j），经销商将商品卖出（i<=j），同时
他还需要付给该仓库j-i元的租金（每天租金为1）。求最多可以赚多少利润。
"""

def best_deal(items: list):
    best_buy_with_storage_cost = items[0]
    max_profit = 0
    for i in range(len(items)):
        best_buy_with_storage_cost += 1
        if items[i] < best_buy_with_storage_cost:
            best_buy_with_storage_cost = items[i]
        max_profit = max(max_profit, items[i] - best_buy_with_storage_cost)

    return max_profit


assert best_deal([2, 1, 5]) == 3
assert best_deal([7, 6, 5]) == 0
assert best_deal([1, 2, 4, 4]) == 1
assert best_deal([1, 6, 3, 7]) == 4
assert best_deal([1, 3]) == 1
