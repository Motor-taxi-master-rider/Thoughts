import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from chi import ChiSquared

expected = [[10]] * 6
observed = [[8], [9], [19], [6], [8], [10]]

chi = ChiSquared(expected, observed)
print(chi)
