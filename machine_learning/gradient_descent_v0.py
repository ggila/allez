import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

hours, pauses, results = [], [], []
data_len = 0

# Get data
with open('./data.txt', 'r') as f:
    for line in f:
        data_len += 1
        value = line.split()
        for i, l in enumerate([hours, pauses, results]):
            l.append(int(value[i]))

for l in [hours, pauses, results]:
    l = np.asarray(l, dtype=float)

# initialize figure
fig = plt.figure()

ax = fig.add_subplot(121, projection='3d')
ax.set_title('given values')
ax.set_xlabel('hours')
ax.set_ylabel('pauses')
ax.set_zlabel('result')

ax2 = fig.add_subplot(122, projection='3d')
ax2.set_title('Cost function')
ax2.set_xlabel('WH')
ax2.set_ylabel('WP')
ax2.set_zlabel('diff')

# Add data to subplot 1
H, P, Z = hours, pauses, results
ax.scatter(H, P, Z, c='r', marker='o')

# We want a function F which, given x hours of work and y number of pauses as inputs, outputs an estimate grade
# - first try :
#       F(h, p) = wh * h + wp * p

# Cost Function
#   J(wh, wp) = 1 / 2m * sum(((wh * hi + wp * pi - yi) ^ 2, i, 0, m - 1)
#   where m is the number of given data, Xi/Yi the input/output of i-th data

WH = np.arange(-5, 5, 0.25)
WP = np.arange(-5, 5, 0.25)
WH, WP = np.meshgrid(WH, WP)

Z = np.zeros(np.shape(WP))
for i in range(data_len):
    Z += 1. / (2 * data_len) * (WH * hours[i] + WP * pauses[i] - results[i])**2

# Plot cost function on subplot 2
ax2.plot_surface(WH, WP, Z, rstride=4, cstride=4, cmap=cm.coolwarm)

# Display figure
plt.show()
