# Zackary Cleveland PHYS3000

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

grid_points = 121 * 50
domain = 100
dx = domain / (grid_points - 1)
time_steps = 1
sigma = 0.5
dt = sigma * dx
c = 1
u = np.ones(grid_points)
u[int(.5 / dx) :int(1 / dx + 1)] = 2


def update(frame) :
    plt.cla()
    for n in range(frame) :
        un = u.copy()
        for i in range(1 , grid_points) :
            u[i] = un[i] - c * dt / dx * (un[i] - un[i - 1])
            # u[i] = un[i] - u[i] * dt / dx * (un[i] - un[i-1])

    plt.plot(np.linspace(0 , domain , grid_points) , u)

    time_elapsed = frame * dt
    plt.text(80 , 1.8 , f'Time Elapsed: {time_elapsed:.3f} s' , fontsize = 10)


fig , ax = plt.subplots()

ani = anim.FuncAnimation(fig , update , interval = 50)
plt.show()
