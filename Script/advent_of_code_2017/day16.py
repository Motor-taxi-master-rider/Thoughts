def solve(A, B):
    mult_a = 16807
    mult_b = 48271
    moder = 2147483647
    bitmap = 2 ** 16 - 1
    count = 0

    for _ in range(5000000):
        A = A * mult_a % moder
        B = B * mult_b % moder
        while A & 3:
            A = A * mult_a % moder
        while B & 7:
            B = B * mult_b % moder
        if A & bitmap == B & bitmap:
            count += 1

    return count


# with open('input.txt', 'r') as f:
#     instructions = [line.split() for line in f.readlines()]
import time

s = time.time()
print(solve(722, 354))
e = time.time()
print(e - s)
