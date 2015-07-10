import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# size of the crowd
N = 5

def gen_data():
    """ init position and speed of each people """
    x = y = np.zeros(N)
    theta = np.random.random(N) * 360 / (2 * np.pi)
    v0 = 1.4
    vx, vy = v0 * np.cos(theta), v0 * np.sin(theta)
    return np.array([x, y, vx, vy]).T

def init():
    pathcol.set_offsets([[], []])
    return pathcol,

def update_lines(i, pathcol, data):
    data[:, 0:2] += data[:, 2:4]
    data[:, 2] = np.where(np.abs(data[:, 0]) > 50, -data[:, 2], data[:, 2])
    data[:, 3] = np.where(np.abs(data[:, 1]) > 50, -data[:, 3], data[:, 3])
    pathcol.set_offsets(data[:, 0:2])
    return [pathcol]

fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
pathcol = plt.scatter([], [], c='k')
data = gen_data()
anim = animation.FuncAnimation(fig, update_lines, init_func=init,
                               fargs=(pathcol, data), interval=50, blit=True)
plt.show()
