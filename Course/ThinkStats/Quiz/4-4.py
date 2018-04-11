import os
import random
import sys

import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

lst = []
for _i in range(1000):
    lst.append(random.paretovariate(1.7) * 100)
mean = np.mean(lst)
print(mean)
print(np.max(lst))
print(np.min(lst))
print((len(list(filter(lambda x: x <mean, lst))))/len(lst))
