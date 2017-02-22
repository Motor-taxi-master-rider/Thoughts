import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import matplotlib.pyplot as pyplot
import random
import numpy as np
import Cdf
import myplot


def Sample(n, u = 950, v = 50):
    return sorted(np.random.normal(u, v, n))

def Samplize(n, f = 1000):
    for i in range(1, n):
        lst = []
        for _i in range(100):
            lst.append(np.amax(Sample(i)))
        if(np.mean(lst) >= f):
            return i,lst


def main():
    result = Samplize(10000)
    mean = np.mean(result[1])
    std = np.std(result[1])
    print(result)
    print("Mean: ", mean)
    print("Standard Deviation: ", std)

    xs = [random.normalvariate(mean, std) for i in range(len(result[1]))]

    xs = Cdf.MakeCdfFromList(xs)
    ys = Cdf.MakeCdfFromList(result[1])

    myplot.Cdf(xs)
    myplot.Cdf(ys)
    myplot.show()

if __name__ == '__main__':
    main()
