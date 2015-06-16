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
fig = plt.figure(figsize=((11,15)))

first = {}
for number, position in enumerate([421, 423, 425, 427]):
    first['ax{0}0'.format(number)] = fig.add_subplot(position, projection='3d')
for elem in first:
    first[elem].set_xlabel('x')
    first[elem].set_ylabel('y')
    first[elem].set_zlabel('z')
    first[elem].scatter(data[:,0], data[:,1], data[:,2], c='r', marker='o')

Wx = np.arange(-5, 5, 0.25)
Wy = np.arange(-5, 5, 0.25)
Wx, Wy = np.meshgrid(Wx, Wy)

Z = np.zeros(np.shape(Wx))
for i in range(data_len):
    Z += 1. / (2 * data_len) * (Wx * data[i,0] + Wy * data[i,1] - data[i,2])**2

second = {}
for number, position in enumerate([422, 424, 426, 428]):
    second['ax{0}1'.format(number)] = fig.add_subplot(position, projection='3d')
    second['ax{0}1'.format(number)].set_xlabel('Wx')
    second['ax{0}1'.format(number)].set_ylabel('Wy')
    second['ax{0}1'.format(number)].set_zlabel('diff')
    second['ax{0}1'.format(number)].plot_surface(Wx, Wy, Z, rstride=4, cstride=4, cmap=cm.coolwarm)


plt.show()
