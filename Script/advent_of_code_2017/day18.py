import threading
import time
from collections import defaultdict
from queue import Empty, Queue

finish = [False, False]
q = [Queue(), Queue()]


def solve(lst, id):
    value = defaultdict(lambda: 0)
    value['p'] = id
    index = 0
    count = 0

    def transfer(item):
        try:
            result = int(item)
        except ValueError:
            result = value[item]
        return result

    while True:
        action = lst[index].split()
        if action[0] == 'set':
            value[action[1]] = transfer(action[2])
        elif action[0] == 'add':
            value[action[1]] += transfer(action[2])
        elif action[0] == 'mul':
            value[action[1]] *= transfer(action[2])
        elif action[0] == 'mod':
            value[action[1]] %= transfer(action[2])
        elif action[0] == 'snd':
            count += 1
            q[id].put(transfer(action[1]))
            print(f'send: {transfer(action[1])} {index} {id}')
        elif action[0] == 'rcv':
            while True:
                try:
                    value[action[1]] = q[1 - id].get_nowait()
                except Empty:
                    if q[0].empty() and q[1].empty():
                        print(id, count)
                        return
                else:
                    print(f'recv: {value[action[1]]} {index} {id}')
                    break
        elif action[0] == 'jgz':
            if value[action[1]] > 0:
                index += transfer(action[2])
                continue
        index += 1


with open('input.txt', 'r') as f:
    lst = [line[:-1] for line in f.readlines()]
print(list(enumerate(lst)))

t0 = threading.Thread(target=solve, args=(lst, 0))
t1 = threading.Thread(target=solve, args=(lst, 1))
t0.start()
t1.start()
t0.join()
t1.join()
# s = time.time()
# print(solve(lst))
# e = time.time()
# print(e - s)
