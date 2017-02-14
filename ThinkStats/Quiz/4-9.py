import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np

def Sample(u = 0, v = 1, n):
    return np.random.normal(u, v, n)

def Samples(n = 6, ):
    list = []
    for _i in range(1000):
        list.append(Sample())
    return list

zipped = []
for sample in Samples():
    if(not zipped):
        zipped = sample
    else:
        zipped = zip(zipped, sample)
print(zipped)

for sample in zipped:
    list = []
    list.append(np.mean(sample))
#print(list)
