import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = y = np.arange(-10, 10, 0.1)
x, y = np.meshgrid(x, y)

z = 30*x + 10*y
ax.plot_surface(x, y, z, rstride=200, cstride=200, alpha=1, color = 'r')

z = x**2 + y**2
ax.plot_surface(x, y, z, rstride=10, cstride=10, cmap=cm.coolwarm)


plt.show()
