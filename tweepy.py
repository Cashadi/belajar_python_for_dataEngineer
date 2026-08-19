import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)

cd = ['clinton', 'trump', 'sanders', 'cruz']

clinton = 156
trump = 250
sanders = 180
cruz = 90

ax = sns.barplot(x=cd, y=[clinton, trump, sanders, cruz])
ax.set(ylabel="count")

plt.show()