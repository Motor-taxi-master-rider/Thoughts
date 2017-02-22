import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import thinkstats

def Biocoin(n, k, p = 1/2):
    return thinkstats.Binom(n, k) * p ** k * (1 - p) ** (n - k)

personP = Biocoin(15, 10)
prob = 1- Biocoin( 10, 10, p = (1 - personP))
print(prob)