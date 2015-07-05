import os
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

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
def batch_gradient_descent(W_batch, alpha):
    for j  in range(n_iter - 1):
        a, b = W_batch[j][0:2]
        temp = a
        a = a - alpha * dJdx(a, b)
        b = b - alpha * dJdy(temp, b)
        W_batch[j + 1] = [a, b, J(a,b)]
    return W_batch

def mini_batch_gradient_descent(W_mini, alpha, data):
    i = 0
    while i < n_iter - 1:
        j = 0
        np.random.shuffle(data)
        print data
        while j < len(data):
            if i+j == n_iter - 1: break
            Wx, Wy = W_batch[i + j][0:2]
            temp = Wx
            Wx = Wx - alpha * 1./data_len\
                * ((Wx * data[j,0] + Wy * data[j,1] - data[j,2]) * data[j,0])
            Wy = Wy - alpha * 1./data_len\
                * ((temp * data[j,0] + Wy * data[j,1] - data[j,2]) * data[j,1])
            W_mini[j+1] = [Wx, Wy, J(Wx, Wy)]
            j += 1
        i += j
    return W_mini

n_iter = 75
alpha = 0.01
W_batch = np.empty((n_iter, 3))
W_mini = np.empty((n_iter, 3))

weight_init = np.empty(3)
weight_init[0] = 4 * np.random.rand()
weight_init[1] = 4 * np.random.rand() - 2
weight_init[2] = J(weight_init[0], weight_init[1])

W_batch[0] = weight_init
W_batch = batch_gradient_descent(W_batch, alpha)

W_mini[0] = weight_init
W_mini = mini_batch_gradient_descent(W_mini, alpha, data)

def fig_config(ax, title, x, y, z=None):
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    if z is not None:
        ax.set_zlabel(z)

# set figure
fig = plt.figure(figsize=((15, 10)))

Wx = np.arange(0, 4, 0.25)
Wy = np.arange(-2, 2, 0.25)
Wx, Wy = np.meshgrid(Wx, Wy)
Z = np.zeros(np.shape(Wx))
Z = v_J(Wx, Wy)

ax1 = plt.subplot2grid((3,3), (0,0), colspan=2, rowspan=2, projection='3d')
fig_config(ax1, 'Cost function', 'Wx', 'Wy', 'J')
ax1.plot_surface(Wx, Wy, Z, rstride=2, cstride=2, cmap=cm.coolwarm, alpha=0.3)

x = [a for a, b in W_batch[:, 0:2]]
y = [b for a, b in W_batch[:, 0:2]]
ax1.plot(x[0:11] , y[0:11], v_J(x, y)[0:11], c='b')
ax1.scatter([x[j] for j in (0, 1, 5, 10, 20)]\
        , [y[j] for j in (0, 1, 5, 10, 20)],\
        [v_J(x, y)[j] for j in (0, 1, 5, 10, 20)]\
        , c='b', marker='o')

ax2 = fig.add_subplot(3,3,3)
fig_config(ax2, 'convergence', 'nb_iteration', 'J')
ax2.set_ylim([0,100])
ax2.plot(W_batch[:, 2], c='r', linewidth=2, label='W_batch')
ax2.plot(W_mini[:, 2], c='b', linewidth=2, label='W_mini')
ax2.legend(loc='upper right')

# Display figure
plt.show()
