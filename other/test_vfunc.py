import os
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Get data
cwd = os.path.dirname(os.path.realpath(__file__)) 
data = np.loadtxt(cwd + '/data.txt', delimiter=' ')
data_len = np.shape(data)[0]

# initialize figure
fig = plt.figure()

Wx = np.arange(-5, 5, 0.25)
Wy = np.arange(-5, 5, 0.25)
Wx, Wy = np.meshgrid(Wx, Wy)

Z = np.zeros(np.shape(Wx))

def cost_func(Wx, Wy):
    return sum(1./ (2 * data_len) * (Wx * data[:,0] + Wy * data[:,1] - data[:,2])**2)
v_cost_func = np.vectorize(cost_func)

Z = v_cost_func(Wx, Wy)

ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Wx')
ax.set_ylabel('Wy')
ax.set_zlabel('diff')
ax.plot_surface(Wx, Wy, Z, rstride=4, cstride=4, cmap=cm.coolwarm)

plt.show()
