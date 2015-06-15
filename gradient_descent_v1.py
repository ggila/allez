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

for name, position in zip(['ax00', 'ax10', 'ax20', 'ax30'], [421, 423, 425, 427]):
    name = fig.add_subplot(position, projection='3d')
    name.set_title('data')
    name.set_xlabel('x')
    name.set_ylabel('y')
    name.set_zlabel('z')
    name.scatter(data[:,0], data[:,1], data[:,2], c='r', marker='o')

Wx = np.arange(-5, 5, 0.25)
Wy = np.arange(-5, 5, 0.25)
Wx, Wy = np.meshgrid(Wx, Wy)

Z = np.zeros(np.shape(Wx))
for i in range(data_len):
    Z += 1. / (2 * data_len) * (Wx * data[i,0] + Wy * data[i,1] - data[i,2])**2

for name, position in zip(['ax01', 'ax11', 'ax21', 'ax31'], [422, 424, 426, 428]):
    name = fig.add_subplot(position, projection='3d')
    name.set_title('Cost function')
    name.set_xlabel('Wx')
    name.set_ylabel('Wy')
    name.set_zlabel('diff')
    name.plot_surface(Wx, Wy, Z, rstride=4, cstride=4, cmap=cm.coolwarm)

# Add data to subplot 1
#H, P, Z = hours, pauses, results

# We want a function F which, given x hours of work and y number of pauses as inputs, outputs an estimate grade
# - first try :
#       F(h, p) = wh * h + wp * p

# Cost Function
#   J(wh, wp) = 1 / 2m * sum(((wh * hi + wp * pi - yi) ^ 2, i, 0, m - 1)
#   where m is the number of given data, Xi/Yi the input/output of i-th data

# Plot cost function on subplot 2

# Display figure
plt.show()
