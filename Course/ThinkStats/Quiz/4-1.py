import sys
sys.path.append('\Python\ThinkStats')
import random
import Cdf
import myplot
import numpy as np

list = []
for i in range(44000):
    list.append(random.expovariate(1 / 32.6))
cdf = Cdf.MakeCdfFromList(list, 'expovariate')
myplot.Cdf(cdf, complement = True,xscale = 'linear',yscale = 'log10')
myplot.show()
