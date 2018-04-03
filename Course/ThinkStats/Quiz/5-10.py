import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import thinkstats

def Biocoin(n, k, p = 1/2):
    return thinkstats.Binom(n, k) * p ** k * (1 - p) ** (n - k)

def main():
    sum = 0
    for i in range(1, 51):
        result = Biocoin(100, i)
        sum += result
    print(sum)

if __name__ == '__main__':
    main()
