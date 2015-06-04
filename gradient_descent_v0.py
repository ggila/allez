import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

hours, pauses, result = [], [], []

# Get data
with open('./data.txt', 'r') as f:
    for line in f:
        value = line.split()
        for i, l in enumerate([hours, pauses, result]):
            l.append(int(value[i]))

for l in [hours, pauses, result]:
    l = np.asarray(l, dtype=float)

# initialize figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Add data to figure
X, Y, Z = hours, pauses, result
ax.scatter(X, Y, Z, c='r', marker='o')

# We want a function F which, given x hours of work and y number of pauses as inputs, outputs an estimate grade
# - first try :
#       F(h, p) = w0 + w1 * h + w2 * p
#       F(X) = t(W) * X

#       where :      W = | w0 |      X = | 1 |
#                        | w1 |          | h |
#                        | w2 |          | p |

# Cost Function
#   (mesure difference beetwen F output and given datas)
#   J(X) = 
#   J(w0, w1, w2) = 1 / 2m * sum((F(Xi) - Yi) ^ 2, i, 0, m)
#   where m is the number of given data, Xi/Yi the input/output of i-th data

# We calculate the weight of F (i.e w0, w1, w2) by finding the minimum of the error

# Display figure
ax.set_xlabel('hours')
ax.set_ylabel('pauses')
ax.set_zlabel('result')
plt.show()
