import functools


def time(func):
    import time
    @functools.wraps(func)
    def warpper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result

    return warpper


def solution(lst, order):
    # 循环数组，start为头指针
    result_list = list(order)
    # 减少Partner时间复杂度的字典
    result_dict = {s: i for i, s in enumerate(result_list)}
    length = len(result_list)
    start = 0

    for action in lst:
        if action.startswith('s'):
            start = (start + length) % length - int(action[1:])
            continue

        if action.startswith('x'):
            x, y = action[1:].split('/')
            x_real = (start + int(x)) % length
            y_real = (start + int(y)) % length
        elif action.startswith('p'):
            x, y = action[1:].split('/')
            x_real = result_dict[x]
            y_real = result_dict[y]
        result_list[x_real], result_list[y_real] = result_list[y_real], result_list[x_real]
        result_dict[result_list[x_real]], result_dict[result_list[y_real]] = result_dict[result_list[y_real]], \
                                                                             result_dict[result_list[x_real]]
    return "".join(result_list[i % length] for i in range(start, start + length))


@time
def solution2(lst):
    orders = []
    order = 'abcdefghijklmnop'
    while order not in orders:
        orders.append(order)
        order = solution(lst, order)

    return orders[1000000000 % len(orders)]


with open(r'../input.txt') as fp:
    lst = fp.read()[:-1].split(',')
print(solution(lst, 'abcdefghijklmnop'))
print(solution2(lst))
