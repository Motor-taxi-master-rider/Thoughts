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


@time
def solution():
    with open(r'input.txt') as fp:
        lst = fp.read().split(',')
    result = [c for c in 'abcdefghijklmnop']
    result_dict = {}
    for i,s in enumerate(lst):
        result_dict[s] = i

    for action in lst:
        if action.startswith('s'):
            for i in range(int(action[1:])):
                pass
        elif action.startswith('x'):
        elif action.startswith('p'):


print(solution())
