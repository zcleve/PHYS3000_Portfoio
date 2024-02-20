import numpy as np
import matplotlib.pyplot as plt
import mathFuncs as mf


# f_lpf returns the numerical soln to the differential eqn
# where Vin is a function of t:
# dVout/dt = (Vin(t)−Vout(t))/RC,
def f_lpf(x, t, r=1e6, c=1e-6):
    tau = c * r
    pi = np.pi
    return mf.sum_of_cos(t,5, 5, 5, 1 / 5) / tau
def f_free_fall_drag(v,t,g=9.81,c=1.225e-3,m=0.142):
    return -g + (c * v**2)


def runge_kutta(func, x0, dt, t0=0, N=10000):
    x_space = np.zeros(N + 1)
    x_space[0] = x0

    t_space = np.linspace(t0, t0 + dt, num=N + 1)
    h = dt / N

    for i in range(N):
        x_iter, t_iter = x_space[i], t_space[i]
        k1 = h * func(x_iter, t_iter)
        k2 = h * func(x_iter + (1 / 2) * k1, t_iter + (1 / 2) * h)
        k3 = h * func(x_iter + (1 / 2) * k2, t_iter + (1 / 2) * h)
        k4 = h * func(x_iter + k3, t_iter + h)
        rk = (1 / 6) * (k1 * 2 * k2 + 2 * k3 + k4)

        x_space[i + 1] = x_iter + rk
    return x_space, t_space


values = runge_kutta(f_lpf, 0, 10, )
fig, ax = plt.subplots()
pi = np.pi

ax.plot(values[1], values[0], color="magenta", label="Output signal")
ax.plot(values[1], ((5 * np.cos((2 * pi * values[1]) / 5) + 5 * np.cos((10 * pi * values[1])))), color="green",
        label="Vin")
ax.set_xlabel("Time (t)")
ax.set_ylabel("Voltage (Vin and Vout)")
#ax.set_ylabel("Velocity in Y")
ax.legend()
plt.show()
