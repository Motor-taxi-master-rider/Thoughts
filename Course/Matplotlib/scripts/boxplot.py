import matplotlib.pyplot as plt
import mpl_toolkits.axes_grid1.inset_locator as mpl_il
import numpy as np
import pandas as pd

normal_sample = np.random.normal(loc=0.0, scale=1.0, size=10000)
random_sample = np.random.random(size=10000)
gamma_sample = np.random.gamma(2, size=10000)

df = pd.DataFrame({'normal': normal_sample,
                   'random': random_sample,
                   'gamma': gamma_sample})
print(df.describe())

plt.figure()
plt.boxplot([ df['normal'], df['random'], df['gamma'] ]
,whis='range')
ax2 = mpl_il.inset_axes(plt.gca(), width='60%', height='40%', loc=2)
ax2.hist(df['gamma'], bins=100)
ax2.margins(x=0.5)
ax2.yaxis.tick_right()

plt.show()
