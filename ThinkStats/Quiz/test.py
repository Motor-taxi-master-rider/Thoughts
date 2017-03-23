import matplotlib.pyplot as plt
import numpy as np

plt.figure()

languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

plt.bar(pos, popularity, align='center')
plt.xticks(pos, languages)
plt.ylabel('% Popularity')
plt.title(
    'Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
ax = plt.axes()
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_ylabel('')
plt.tick_params(top='off', bottom='off',
                left='off', right='off', labelleft='off', labelbottom='on')
# TODO: remove all the ticks (both axes), and tick labels on the Y axis

plt.show()
