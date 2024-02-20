# Zackary Cleveland PHYS3000

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as anim

grid_points = 81
domain = 10
c = 1
dx = domain / (grid_points - 1)
dy = domain / (grid_points - 1)

sigma = 0.2
dt = sigma * dx

x = np.linspace(0, domain, grid_points)
y = np.linspace(0, domain, grid_points)

u = np.ones((grid_points, grid_points))
u[int(0.5 / dy):int(1 / dy + 1), int(0.5 / dx):int(1 / dx + 1)] = 2

fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(x, y)
surf = ax.plot_surface(X, Y, u, cmap=cm.viridis)

def update(frame, u):
    global surf
    #row, col = u.shape
    un = u.copy()
    u[1 : , 1 :] = (un[1 : , 1 :] - (c * dt / dx * (un[1 : , 1 :] - un[1 : , :-1])) -
                    (c * dt / dy * (un[1 : , 1 :] - un[:-1 , 1 :])))
    u[0 , :] = 1
    u[-1 , :] = 1
    u[: , 0] = 1
    u[: , -1] = 1
    surf.remove()  # Remove the old surface plot
    ax.clear()
    surf = ax.plot_surface(X, Y, u, cmap=cm.viridis)
    time_elapsed = frame * dt
    ax.text2D(0.05, 0.95, f'Time Elapsed: {time_elapsed:.3f} s', transform=ax.transAxes, fontsize=10, color='red')
    return surf,

ani = anim.FuncAnimation(fig, update, fargs=(u,), interval=50)
plt.show()



