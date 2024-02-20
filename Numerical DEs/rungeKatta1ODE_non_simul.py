import numpy as np

def runge_kutta(func, x0, dt, t0=0, N=1000):
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