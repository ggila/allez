from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

x = np.array([-10,-10,10,10])
y = np.array([-10,-10,10,10])
z = np.array([0,10,0,10])

ax.plot_surface(x, y, z)

plt.show()

