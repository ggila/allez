import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(-5,5),ylim=(-5,5))
lines = [plt.plot([],[], 'o')[0] for i in range(3)]

x = np.linspace(-5,5,200)
y1, y2, y3 =  np.array([-0.2*x**2-1.8, 0.2*x**2+2, np.cos(x)])
data = x, y1, y2, y3

def init():
    for line in lines:
        line.set_data([],[])
    return lines

def update_lines(i, lines, data):
    i %= 200
    x = data[0]
    for line, y in zip(lines, data[1:4]):
        line.set_data(x[i],y[i])
    return lines

anim = animation.FuncAnimation(fig, update_lines, init_func=init, fargs=(lines, data), frames=200, interval=20, blit=True)
#anim = animation.FuncAnimation(fig, update_line, fargs=(x, line), frames=20, interval=200, blit=True)

plt.show()
