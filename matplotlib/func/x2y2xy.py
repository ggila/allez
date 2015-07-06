import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = y = np.arange(-100, 100, 1)
x, y = np.meshgrid(x, y)

z = (x+y)**2 + 6*(x+y) + 4

ax.plot_surface(x, y, z)

plt.show()
