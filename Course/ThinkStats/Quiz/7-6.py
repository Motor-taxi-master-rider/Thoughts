import os
import sys

from chi import ChiSquared

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


expected = [[10]] * 6
observed = [[8], [9], [19], [6], [8], [10]]

chi = ChiSquared(expected, observed)
print(chi)
