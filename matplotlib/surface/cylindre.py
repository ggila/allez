from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 1.5 * np.pi, 100)

x = 5 * np.cos(u)
y = 5 * np.sin(u)
x = np.repeat(x[..., np.newaxis], 2, axis=1)
y = np.repeat(y[..., np.newaxis], 2, axis=1)
z = np.meshgrid(np.array([-10,10]), np.arange(100))[0]
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')

plt.show()

