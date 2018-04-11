import os
import sys

import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def Sample(n, u = 0, v = 1):
    return sorted(np.random.normal(u, v, n))

def Samples(n = 6, m = 1000):
    return [Sample(n) for i in range(m)]

t = zip(*Samples())

print(sorted([np.mean(sample) for sample in t]))
