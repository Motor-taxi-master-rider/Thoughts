"""
Problem:
先手最高得分
有N张卡牌堆成一摞，每张卡牌上都会有一个整数标记其分数。
现有两个人要交替从牌堆顶拿牌，每次至少拿一张，至多拿M张，直到牌堆被拿完。
每个人拿至手中的牌的分数和即为其最终得分。假设两个人都会采取最佳策略拿牌来使自己的得分最大化，请问先手拿牌的人的得分为多少？

输入描述
对于每个样例，第一行是N，M，第二行有O个整数，代表牌堆顶到牌堆底O张牌的分数。
0 < N, M，O < 1,000,000,  每张牌的分数在-100和100之间

输出描述
每个样例，输出一个整数代表先手得分。

示例1:

输入
4 2
1 1 1 1

输出
2

示例2:

输入
5 2
3 -4 1 1 7

输出
6
说明: 第一个样例，先手拿2张1，最高得分为2。 第二个样例，先手拿3，-4，
逼迫对方接下来只能拿1，1，最后自己再拿到7，所以先手最高得分为6。
"""

from itertools import repeat


def card_max_score(remain, max_choice, deck):
    scores = list(repeat(None, remain))
    scores[-1] = deck[-1]
    i = remain - 1
    # 当可选元素大于最大可选元素时可以得出最优的选择方式
    while i >= remain - max_choice:
        max_score = None
        best_choice = 1
        j = 1
        while j <= max_choice and i + j <= remain:
            score = sum(deck[i:i + j])
            if max_score is None or score > max_score:
                max_score = score
                best_choice = j
            j += 1
        scores[i] = (best_choice, max_score)
        i -= 1

    # 递推推导出从后X张牌中得到最大分数的结果
    i = remain - max_choice - 1
    while i >= 0:
        max_score = None
        best_choice = 1
        j = 1
        while j <= max_choice:
            picked_score = sum(deck[i:i + j])
            opp_choice, _ = scores[i + j]  # 对方按照最佳策略选择opp_choice张卡牌
            next_index = i + j + opp_choice  # 我方下一个问题空间减少这次选择的数量+对方选择的数量
            if next_index < remain:
                _, next_score = scores[next_index]
                score = picked_score + next_score
            else:
                score = picked_score
            if max_score is None or score > max_score:
                max_score = score
                best_choice = j
            j += 1
        scores[i] = (best_choice, max_score)
        i -= 1

    return scores[0][1]


assert card_max_score(5, 2, [3, -4, 1, 1, 7]) == 6
assert card_max_score(4, 2, [1, 1, 1, 1]) == 2

# Recursion solution
# def solve(remain, max_choice, deck):
#     if max_choice < 1:
#         raise ValueError()
#     if max_choice >= remain:
#         best_choice = 1
#         best_score = None
#         best_diff = None
#         for i in range(1, max_choice + 1):
#             my_score = sum(deck[:i])
#             his_score = sum(deck[i:])
#             diff = my_score - his_score
#             if best_diff is None or diff > best_diff:
#                 best_diff = diff
#                 best_score = my_score
#                 best_choice = i
#         return best_choice, best_score
#
#     best_choice = 1
#     best_score = None
#     for i in range(1, max_choice + 1):
#         his_choice, _ = solve(remain - i, max_choice, deck[i:])
#         my_choice, my_score = solve(remain - i, max_choice, deck[i + his_choice:])
#         my_score = sum(deck[:i]) + my_score
#         if best_score is None or my_score > best_score:
#             best_score = my_score
#             best_choice = i
#     return best_choice, best_score
#
# a = solve(5, 2, [3,-4,1,1,7])
# print(a)
