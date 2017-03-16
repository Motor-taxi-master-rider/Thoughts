import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np


def SampleVarError(u=0, v=1, n=6):
    sample = np.random.normal(u, v, n)
    return np.var(sample) - v


def SampleVarError2(u=0, v=1, n=6):
    sample = np.random.normal(u, v, n)
    return np.var(sample) * n / (n - 1) - v


def SampleVarSquaredError(n=1000, func=SampleVarError2):
    return np.sum([func() for i in range(n)]) / n


def BiasVarSquaredError(n=1000, func=SampleVarError):
    return np.sum([func() for i in range(n)]) / n


def main():
    varError = SampleVarSquaredError()
    biasvarError = BiasVarSquaredError()
    print(varError)
    print(biasvarError)


if __name__ == "__main__":
    main()
