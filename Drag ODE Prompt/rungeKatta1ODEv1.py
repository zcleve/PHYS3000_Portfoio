import numpy as np

# takes an input function with starting 'x' condition, final time, and time steps/iterations, as well as function
# arguments. and returns the numerically approximated x,t values over t.
# Essentially solves 1st order IVP ODEs given (x0, t0)
def runge_kutta(func, x0, tf,  args=(), t0 = 0 , dt = 1000) :
    # creates an array to hold all the future calculated values of 'x' based on the time steps argument
    x_space = np.zeros(dt + 1)

    # applies the initial value condition
    x_space[t0] = x0

    # generates the values of t given the final time specified and the time steps
    # plus one bc array index start at 0
    t_space = np.linspace(tf , num = dt + 1)

    # creates the runge katta step size
    h = tf / dt

    # iterates the runge katta 4th order method across the x,t arrays
    for i in range(dt) :
        x_iter , t_iter = x_space[i] , t_space[i]
        k1 = h * func(x_iter , t_iter, *args)
        k2 = h * func(x_iter + (1 / 2) * k1 , t_iter + (1 / 2) * h, *args)
        k3 = h * func(x_iter + (1 / 2) * k2 , t_iter + (1 / 2) * h, *args)
        k4 = h * func(x_iter + k3 , t_iter + h, *args)
        rk = (1 / 6) * (k1 * 2 * k2 + 2 * k3 + k4)

        x_space[i + 1] = x_iter + rk
    return x_space , t_space
