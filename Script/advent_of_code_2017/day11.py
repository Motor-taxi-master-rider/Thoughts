from collections import Counter


def switcher(direction):
    return {'n': lambda x, y: (x, y + 1),
            's': lambda x, y: (x, y - 1),
            'nw': lambda x, y: (x - 1, y - 0.5),
            'ne': lambda x, y: (x + 1, y - 0.5),
            'sw': lambda x, y: (x - 1, y + 0.5),
            'se': lambda x, y: (x + 1, y + 0.5)}.get(
        direction, None)


def solution(lst):
    x, y = 0, 0
    for direction in lst:
        x, y = switcher(direction)(x, y)
    if 0.5 * abs(x) > abs(y):
        return abs(x)
    else:
        return 0.5 * abs(x) + abs(y)


def solution2(lst):
    def test(x, y):
        return 0.5 * x > y

    x, y = 0, 0
    x_func = lambda x, y: abs(x)
    y_func = lambda x, y: 0.5 * abs(x) + abs(y)
    x_max = 0
    for direction in lst:
        x, y = switcher(direction)(x, y)
        distance = x_func(x, y)
        if distance > x_max:
            x_max = distance
            x_x = abs(x)
            x_y = abs(y)
    y_max = 0
    x, y = 0, 0
    for direction in lst:
        x, y = switcher(direction)(x, y)
        distance = y_func(x, y)
        if distance > y_max:
            y_max = distance
            y_x = abs(x)
            y_y = abs(y)
    if not test(x_x, x_y):
        x_max = 0
    if test(y_x, y_y):
        y_max = 0
    return max(x_max, y_max)


with open(r'C:\Users\D\Desktop\input.txt') as fp:
    lst = fp.read().split(',')
    lst.pop()

print(solution2(lst))
