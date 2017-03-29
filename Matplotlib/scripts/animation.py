import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.animation as animation

n=100
x=np.random.randn(n)

def update(curr):
    if curr==n:
        a.event_source.stop()
    plt.cla()
    bins=np.arange(-4,4,0.5)
    plt.hist(x[:curr],bins=bins)
    plt.axis([-4,4,0,30])
    plt.annotate('n={}'.format(curr),[3,27])

fig=plt.figure()
a=animation.FuncAnimation(fig,update,interval=10)

plt.show()
