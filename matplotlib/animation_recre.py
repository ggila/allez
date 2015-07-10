import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(-5,5),ylim=(-5,5))
lines = [plt.plot([],[], 'o')[0] for i in range(10)]

x = np.linspace(-5,5,200)
y = 2 * np.random.rand(10) - 1

def init():
    for line in lines:
        line.set_data([],[])
    return lines

def update_lines(i, lines, x, y):
    i %= 200
    for line, a in zip(lines, y):
        line.set_data(x[i],a * x[i])
    return lines

anim = animation.FuncAnimation(fig, update_lines, init_func=init, fargs=(lines, x, y), frames=200, interval=20, blit=True)
#anim = animation.FuncAnimation(fig, update_line, fargs=(x, line), frames=20, interval=200, blit=True)

plt.show()
