import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data=np.random.rand(4, 50, 150)
Z=np.arange(0,120,.8)

fig, axes = plt.subplots(2,2)

lines=[]

for nd, ax in enumerate(axes.flatten()):
    l, = ax.plot(data[nd,0], Z)
    lines.append(l)

def run(it):
    print(it)
    for nd, line in enumerate(lines):
        line.set_data(data[nd, it], Z)
    return lines


ani=animation.FuncAnimation(fig, run, frames=np.arange(0,data.shape[1]),
                            interval=30, blit=True)

plt.show()
