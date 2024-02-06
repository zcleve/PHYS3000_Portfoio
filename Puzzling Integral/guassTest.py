# Zackary Cleveland PHYS3000
import numpy as np


def f(z, k) :
    x = (z / (1 - z))
    dz = 1 / ((1 - z) ** 2)
    f = 1
    for i in range(1,k+1):
        f*= np.sin(x / (2 * i - 1)) / (x / (2 * i - 1))
    return f * dz


def gauss_legendre(N , a , b) :
    # sample and weights from numpy polynomial library, specifically the legendre series
    X , w = np.polynomial.legendre.leggauss(N)
    # map x and w to the domain
    X_map = .5*(b-a)*X + .5*(b+a)
    w_map = .5*(b-a)*w
    I = 0
    for i in range(N):
        I += w_map[i]*f(X_map[i],8)
    return I


N = 2500
print('Error in', N, 'Steps:', gauss_legendre(N, 0.0, 1.0) - np.pi/2)
# this is slow and a lot of terms, but returns -2.3104629320869208e-11, which is damn close