import os
import sys

import numpy as np

import irs

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def main(script, *args):
    data = irs.ReadIncomeFile()
    hist, pmf, cdf = irs.MakeIncomeDist(data)
    SummarizeData(pmf, cdf)


if __name__ == "__main__":
    main(*sys.argv)
