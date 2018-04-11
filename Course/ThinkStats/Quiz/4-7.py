import os
import sys

import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

lst = np.random.normal(100,15,60000000)

def GreaterPercent(lst,num):
    return len(list(filter(lambda x: x > num, lst))) / len(lst)

print(lst.mean())
print(GreaterPercent(lst,lst.mean()))
print( GreaterPercent(lst,115))
print(GreaterPercent(lst,130))
print( GreaterPercent(lst,145))
print( GreaterPercent(lst,190))
