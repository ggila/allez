import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def gen_data():
    x = y = 0
    theta = np.random.random() * 360 / (2 * np.pi)
    v0 = 0.1
    vx, vy = v0 * np.cos(theta), v0 * np.sin(theta)
    return np.array([x, y, vx, vy])

def init():
    line.set_data([],[])
    return line,

def update_line(i, line, data):
    data[0:2] += data[2:4]
#    if abs(data[0]) > 5: data[2] *= -1
#    if abs(data[1]) > 5: data[3] *= -1
    if abs(data[0]) > 5 or abs(data[1]) > 5:
        data[:] = gen_data()
    line.set_data(data[0] ,data[1])
    return line,

fig = plt.figure()
ax = plt.axes(xlim=(-5,5),ylim=(-5,5))
line, = plt.plot([],[], 'o')

data = gen_data()
anim = animation.FuncAnimation(fig, update_line, init_func=init, fargs=(line, data), interval=10, blit=True)

plt.show()
