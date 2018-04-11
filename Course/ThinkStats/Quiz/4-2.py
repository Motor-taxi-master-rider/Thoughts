import os
import random
import sys

import numpy as np

import Cdf
import myplot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

list = []
for _i in range(100):
    list.append(random.expovariate(1))
cdf = Cdf.MakeCdfFromList(list)
myplot.Cdf(cdf,complement=True)

myplot.Show(xscale='linear',yscale='log')
