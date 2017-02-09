import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import random
import numpy as np
import Cdf
import myplot

list = []
for _i in range(44):
    list.append(random.paretovariate(1 / 32.6))
cdf = Cdf.MakeCdfFromList(list)
myplot.Cdf(cdf,complement=True)

myplot.Show(xscale='linear',yscale='log')
