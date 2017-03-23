import matplotlib.pyplot as plt
import numpy as np

plt.figure()

languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]
bars = plt.bar(pos, popularity, align='center',
               linewidth=0, color='lightslategrey')
plt.xticks(pos, languages, alpha=0.8)
plt.ylabel('% Popularity')
plt.title(
    'Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
ax = plt.gca()
# ax.set_xticks([])
# ax.set_yticks([])
#ax.set_ylabel('')
# ax.spines['top'].set_visible(False)
plt.tick_params(top='off', bottom='off',
                left='off', right='off', labelleft='off', labelbottom='on')
for spine in plt.gca().spines.values():
    spine.set_visible(False)
bars[0].set_color('#1F77B4')
for rect, label in zip(ax.patches, popularity):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height -
            5, str(label) + '%', ha='center', va='bottom')

plt.show()
