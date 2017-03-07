import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
import irs


def main(script, *args):
    data = irs.ReadIncomeFile()
    hist, pmf, cdf = irs.MakeIncomeDist(data)
    SummarizeData(pmf, cdf)


if __name__ == "__main__":
    main(*sys.argv)
