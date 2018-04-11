import os
import sys

import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def SampleMeanError(u=0, v=1, n=6):
    sample = np.random.normal(u, v, n)
    return np.mean(sample) - u


def SampleMedianError(u=0, v=1, n=6):
    sample = np.random.normal(u, v, n)
    return np.median(sample) - u


def MeanSquaredError(n=1000, func=SampleMeanError):
    return np.sum([func() ** 2 for i in range(n)]) / n


def main():
    meanError = MeanSquaredError(n=1000000)
    medianError = MeanSquaredError(func=SampleMedianError)
    print(meanError)
    print(medianError)


if __name__ == "__main__":
    main()
