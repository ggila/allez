import os
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# cost_func
def J(Wx, Wy):
    return sum(1./ (2 * data_len)\
            * (Wx * data[:,0] + Wy * data[:,1] - data[:,2])**2)
v_J = np.vectorize(J)

# dJ/dWi
def dJdx(Wx, Wy):
    return 1./data_len\
            * sum((Wx * data[:,0] + Wy * data[:,1] - data[:,2]) * data[:,1])
def dJdy(Wx, Wy):
    return 1./data_len\
            * sum((Wx * data[:,0] + Wy * data[:,1] - data[:,2]) * data[:,2])

# gradient_descent
def gradient_descent(Wlist):
    for i in range(n_iter):
        a, b = Wlist[i]
        a = a - alpha * dJdx(a, b)
        b = b - alpha * dJdy(a, b)
        Wlist.append([a, b])
    return Wlist


# Get data
cwd = os.path.dirname(os.path.realpath(__file__)) 
data = np.loadtxt(cwd + '/data.txt', delimiter=' ')
data_len = np.shape(data)[0]

# cost_func
def J(Wx, Wy):
    return sum(1./ (2 * data_len)\
            * (Wx * data[:,0] + Wy * data[:,1] - data[:,2])**2)
v_J = np.vectorize(J)

# dJ/dWi
def dJdx(Wx, Wy):
    return 1./data_len\
            * sum((Wx * data[:,0] + Wy * data[:,1] - data[:,2]) * data[:,0])
def dJdy(Wx, Wy):
    return 1./data_len\
            * sum((Wx * data[:,0] + Wy * data[:,1] - data[:,2]) * data[:,1])

# gradient_descent
def batch_gradient_descent(Wlist):
    it = ((i, j) for i in range(len(alpha)) for j in range(n_iter - 1))
    for i, j in it:
        a, b = Wlist[i][j][0:2]
        a = a - alpha[i] * dJdx(a, b)
        b = b - alpha[i] * dJdy(a, b)
        Wlist[i, j + 1] = [a, b, J(a,b)]
    return Wlist

#def stochastic_gradient_descent(Wlist):

n_iter = 100
alpha = [0.04, 0.01, 0.001]
Wlist = np.empty((len(alpha), n_iter, 3))

weight_init = 10 * np.random.rand(3) - 5
weight_init[2] = J(weight_init[0], weight_init[1])
for i in range(len(alpha)):
    Wlist[i][0] = weight_init
Wlist = batch_gradient_descent(Wlist)

def fig_config(ax, title, x, y, z=None):
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    if z is not None:
        ax.set_zlabel(z)

# set figure
fig = plt.figure(figsize=((15, 10)))

Wx = np.arange(-5, 5, 0.25)
Wy = np.arange(-5, 5, 0.25)
Wx, Wy = np.meshgrid(Wx, Wy)
Z = np.zeros(np.shape(Wx))
Z = v_J(Wx, Wy)

ax1 = fig.add_subplot(231, projection='3d')
fig_config(ax1, 'Cost function', 'Wx', 'Wy', 'J')
ax1.plot_surface(Wx, Wy, Z, rstride=4, cstride=4, cmap=cm.coolwarm, alpha=0.3)
x = [a for a, b in Wlist[1, :, 0:2]]
y = [b for a, b in Wlist[1, :, 0:2]]
ax1.plot(x , y, v_J(x, y))
ax1.scatter([x[i] for i in (0, 1, 5, 10, 20)]\
        , [y[i] for i in (0, 1, 5, 10, 20)],\
        [v_J(x, y)[i] for i in (0, 1, 5, 10, 20)]\
        , c='r', marker='o')

ax2 = fig.add_subplot(233)
fig_config(ax2, 'convergence', 'nb_iteration', 'J')
ax2.plot(Wlist[0, :, 2], c='r')
ax2.plot(Wlist[1, :, 2], c='g')
ax2.plot(Wlist[2, :, 2], c='b')

x = np.linspace(0, 14, 50)
y = np.linspace(0, 10, 50)
x, y = np.meshgrid(x, y)

def set_result(ax, nb_iter):
    fig_config(ax, 'After ' + str(nb_iter) + ' iter', 'x', 'y', 'z')
    ax.scatter(data[:,0], data[:,1], data[:,2], c='r', marker='o')
    z = Wlist[1][nb_iter][0] * x + Wlist[1][nb_iter][1] * y
    ax.plot_surface(x, y, z, alpha=0.4)

ax3 = fig.add_subplot(234, projection='3d')
set_result(ax3, 0)
ax4 = fig.add_subplot(235, projection='3d')
set_result(ax4, 10)
ax5 = fig.add_subplot(236, projection='3d')
set_result(ax5, 50)

# Display figure
plt.show()
