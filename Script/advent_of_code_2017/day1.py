def solution():
    with open(r'C:\Users\D\Desktop\input.txt') as fp:
        first = fp.read(1)
        prev = first
        next = fp.read(1)
        result = []
        while next != '\n':
            if prev == next:
                result.append(int(next))
            prev, next = next, fp.read(1)
        if first == prev:
            result.append(int(first))
        print(sum(result))


solution()
