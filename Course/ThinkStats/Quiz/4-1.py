import random
import sys

import numpy as np

import Cdf
import myplot

sys.path.append('\Python\ThinkStats')

list = []
for i in range(44000):
    list.append(random.expovariate(1 / 32.6))
cdf = Cdf.MakeCdfFromList(list, 'expovariate')
myplot.Cdf(cdf, complement = True,xscale = 'linear',yscale = 'log10')
myplot.show()
