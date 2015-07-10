import numpy as np
import matplotlib.pyplot as plt
import itertools

fig, axes = plt.subplots(4,4)

for (i, j) in  itertools.product(range(4), range(4)):
    ax = axes[i][j]
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    if i == j:
        ax.text(0,0,'abc')
        continue
    ax.plot(np.random.random(5), np.random.random(5), 'ko')

plt.show()
