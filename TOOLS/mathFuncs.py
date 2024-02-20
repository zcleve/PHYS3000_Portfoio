import numpy as np

pi = np.pi


def sum_of_cos(x,a1, a2, T1, T2):
    return a1 * np.cos(x*2 * pi / T1) + a2 * np.cos(x*2 * pi / T2)


def difference_of_cos(x,a1, a2, T1, T2):
    return sum_of_cos(x,a1, -a2, T1, T2)
