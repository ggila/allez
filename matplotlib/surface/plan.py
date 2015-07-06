from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


x = np.array([-1, 1])
y = np.array([-1,1])
x = np.repeat(x[..., np.newaxis], 2, axis=1)
y = np.repeat(y[..., np.newaxis], 2, axis=1)
z = np.meshgrid(np.array([-1,1]), np.arange(2))[0]
ax.plot_surface(x, y, z, color='b', alpha=0.3)

plt.show()

