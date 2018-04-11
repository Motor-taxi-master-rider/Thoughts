import sys

import descriptive
import Pmf

sys.path.append('\Myfile\TRAINING\Course\Python\ThinkStats')

def ProbRange(pmf, low, high):
    total=0.0
    for week in range(low, high + 1):
        total += pmf.Prob(week)
    return total

def ProbEarly(pmf):
    if isinstance(pmf,Pmf.Pmf):
        return ProbRange(pmf,0,37)
    else:
        print('Error')
        return

def ProbOnTime(pmf):
    if isinstance(pmf,Pmf.Pmf):
        return ProbRange(pmf,38,40)
    else:
        print('Error')
        return

def ProbOnTime(pmf):
    if isinstance(pmf,Pmf.Pmf):
        return ProbRange(pmf,38,40)
    else:
        print('Error')
        return

def ProbOnTime(pmf):
    if isinstance(pmf,Pmf.Pmf):
        return ProbRange(pmf,38,40)
    else:
        print('Error')
        return

def ProbLate(pmf):
    if isinstance(pmf,Pmf.Pmf):
        return ProbRange(pmf,41,100)
    else:
        print('Error')
        return

def ComputeRelativeRisk(*pmfs):
    print('Risks:')
    risks = {}
    functions = [ProbEarly, ProbOnTime, ProbLate]
    for func in functions:
        for pmf in pmfs:
            prob = func(pmf)
            risks[func.__name__, pmf.name] = prob
            print(func.__name__, pmf.name, prob)
    print(risks)
    print()
    print('Relative Risks:')
    for func in functions:
        try:
            ratio = risks[func.__name__, pmfs[0].name] /  risks[func.__name__, pmfs[1].name]
            print(func.__name__, ratio)
        except ZeroDivisionError:
            pass

def main():
    pool, firsts, others = descriptive.MakeTables()
    ComputeRelativeRisk(firsts.pmf, others.pmf)


if __name__ == "__main__":
    main()
