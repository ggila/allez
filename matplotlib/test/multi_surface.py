import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = y = np.arange(-100, 100, 1)
x, y = np.meshgrid(x, y)

z = (x+y)**2 + 6*(x+y) + 4

ax.plot_surface(x, y, z, rstride=200, cstride=200)

a = np.array([-100, 100])
b = np.array([100,-100])
a = np.repeat(a[..., np.newaxis], 2, axis=1)
b = np.repeat(b[..., np.newaxis], 2, axis=1)
c = np.meshgrid(np.array([-5000,40000]), np.arange(2))[0]

ax.plot_surface(a, b, c, color='r', alpha=0.3)


plt.show()
