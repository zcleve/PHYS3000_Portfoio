import numpy as np


# example function of returning the output voltage of a lowpass filter consisting of initially a micro-farad
# capacitor and a mega-ohm resistor. Takes both constants and functions for the input signal/voltage.
def f_lpf(f , v , t , r = 1e6 , c = 1e-6 , args = ()) :
    tau = c * r
    pi = np.pi
    return f(*args) / tau


# function to return dV/dt in terms of V, i.e. the 1st ODE form of drag
# meant to be used with a numerical ODE solver, i.e. rungeKatta1ODE
# derived from F=−mg+cv^2
def f_free_fall_drag(v , t , c , m , g = 9.81) :
    return -g + ((c * v ** 2) / m)


# free fall of an object without drag, a = -g
def f_free_fall(a , b , g = 9.81) :
    return -g
