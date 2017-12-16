class ReverseList:
    def __init__(self, lst):
        self.lst = lst
        self.skip_size = -1

    def reverse(self, position, length):
        n = position + length
        if n > len(self):
            pos = position
            for item in reversed([self[i % len(self)] for i in range(position, n)]):
                self[pos % len(self)] = item
                pos += 1
        else:
            self.lst[position:n] = reversed(lst[position:position + length])
        self.skip_size += 1

    def __getitem__(self, item):
        return self.lst[item]

    def __setitem__(self, key, value):
        self.lst[key] = value

    def __iter__(self):
        return iter(self.lst)

    def __len__(self):
        return len(self.lst)


def solution(items, lst):
    index = 0
    for item in items:
        lst.reverse(index, item)
        index = (index + item + lst.skip_size) % len(lst)
        print(lst.lst)
    return lst[0] * lst[1]

def solution2(items, lst):
    index = 0
    for item in items:
        lst.reverse(index, item)
        index = (index + item + lst.skip_size) % len(lst)
        print(lst.lst)
    return lst[0] * lst[1]

with open(r'C:\Users\D\Desktop\input.txt') as fp:
    items = [int(s) for s in fp.read().split(',')]
    lst = ReverseList(list(range(256)))

items=[]

print(solution(items, lst))
