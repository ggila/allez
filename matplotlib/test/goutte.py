import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = y = np.arange(-10, 10, 0.1)
x, y = np.meshgrid(x, y)

n = x**2+y**2

z = 5*np.sin(n/5)/n
ax.set_zlim([-0.7, 1])
ax.plot_surface(x, y, z, cmap=cm.coolwarm, rstride=10, cstride=10, alpha=1)

plt.show()
