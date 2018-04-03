import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
import survey


def Skewness(t):
    mean = np.mean(t)
    var = np.var(t)
    return np.mean([((x - mean) / var) ** 3 for x in t if t is not None])

def main():
    table = survey.Pregnancies()
    table.ReadRecords('.')
    prglength = [p.prglength for p in table.records]
    weight = [p.finalwgt for p in table.records]
    print(Skewness(prglength))
    print(Skewness(weight))



if __name__ == '__main__':
    main()
