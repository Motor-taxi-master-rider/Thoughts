import sys
sys.path.append('\Myfile\TRAINING\Course\Python\ThinkStats')
import Pmf
import descriptive
import myplot
import matplotlib.pyplot as pyplot

def MakeFigure(*pmfs):
    weeks = range(35, 46)

    # probs is a map from table name to list of conditional probabilities
    probs = {}
    for pmf in pmfs:
        name = pmf.name
        probs[name] = []
        for week in weeks:
            def filter_func(x):
                return x < week
            cond = ConditionPmf(pmf, filter_func)
            prob = cond.Prob(week)
            print( week, prob, pmf.name)
            probs[name].append(prob)

    # make a plot with one line for each table
    pyplot.clf()
    for name, ps in probs.items():
        pyplot.plot(weeks, ps, label=name)
        print (name, ps)
    myplot.Save(root='conditional',
                xlabel='weeks',
                ylabel=r'Prob{x $=$ weeks | x $\geq$ weeks}',
                title='Conditional Probability')


def ConditionPmf(pmf, filter_func, name = 'conditional'):
    cond_pmf = pmf.Copy()
    vals = [val for val in pmf.Values() if filter_func(val)]
    for val in vals:
        cond_pmf.Remove(val)
    cond_pmf.Normalize()
    return cond_pmf

def Compute(*pmfs, birthweek = 39):
    def filter_func(x):
        return x < birthweek

    for pmf in pmfs:
        prob = ConditionPmf(pmf, filter_func).Prob(birthweek)
        print(pmf.name, 'will be in', birthweek, 'week\'s probability is ', prob)

def main():
    pool, firsts, others = descriptive.MakeTables()
    Compute(firsts.pmf, others.pmf)
    MakeFigure(firsts.pmf, others.pmf)


if __name__ == "__main__":
    main()
