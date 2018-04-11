import sys

import Pmf

sys.path.append('\Myfile\TRAINING\Course\Python\ThinkStats')

pmf=Pmf.MakePmfFromList([1,2,2,3,5])
print(Pmf.PmfMean(pmf))
print(Pmf.PmfVar(pmf))
print(pmf.Var())
