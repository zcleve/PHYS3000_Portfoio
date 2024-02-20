import numpy as np
import mathFuncs as mf

def f_lpf(v, t, r=1e6, c=1e-6):
    tau = c * r
    pi = np.pi
    return mf.sum_of_cos(t,5, 5, 5, 1 / 5) / tau

def f_free_fall_drag(v,t,g=9.81,c=1.225e-3,m=0.142):
    return -g + (c * v**2)