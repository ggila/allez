import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

hours, pauses, results = [], [], []

# Get data
with open('./data.txt', 'r') as f:
    for line in f:
        value = line.split()
        for i, l in enumerate([hours, pauses, results]):
            l.append(int(value[i]))

for l in [hours, pauses, results]:
    l = np.asarray(l, dtype=float)

# initialize figure
fig = plt.figure()
#fig = plt.figure(figsize=plt.figaspect(2.))

# Add data to figure
H, P, Z = hours, pauses, results
ax = fig.add_subplot(121, projection='3d')
ax.scatter(H, P, Z, c='r', marker='o')
ax.set_xlabel('hours')
ax.set_ylabel('pauses')
ax.set_zlabel('result')
ax.plot_surface(H, P, Z)

# We want a function F which, given x hours of work and y number of pauses as inputs, outputs an estimate grade
# - first try :
#       F(h, p) = wh * h + wp * p

# Cost Function
#   J(wh, wp) = 1 / 2m * sum(((wh * hi + wp * pi - yi) ^ 2, i, 0, m - 1)
#   where m is the number of given data, Xi/Yi the input/output of i-th data

WH = np.arange(-5, 5, 0.25)
WP = np.arange(-5, 5, 0.25)
WH, WP = np.meshgrid(WH, WP)

m = len(hours)

Z = np.zeros(np.shape(WP))
for i in range(m):
    Z += 1. / (2 * m) * (WH * hours[i] + WP * pauses[i] - results[i])**2

ax2 = fig.add_subplot(122, projection='3d')
ax2.set_title('Cost function')
ax2.plot_surface(WH, WP, Z, rstride=4, cstride=4, cmap=cm.coolwarm)

# We calculate the weight of F (i.e wh, wp) by finding the minimum of the error. We find minimum of J by gradient descent :
# We repeateadly update weight :
# wj = wj - alpha * dJ(W)/d(wj)  for every j in [0, m-1]
# where alpha is the learning step
# wj = wj - alpha / m * sum(())

# Display figure
plt.show()
