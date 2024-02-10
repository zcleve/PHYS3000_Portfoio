# Zackary Cleveland PHYS3000
import numpy as np

def gauss_legendre(f, N , bound, k):
    # sample and weights from numpy polynomial library, specifically the legendre series
    X , w = np.polynomial.legendre.leggauss(N)
    # map x and w to the domain
    X_map = .5*(bound[1]-bound[0])*X + .5*(bound[1]+bound[0])
    w_map = .5*(bound[1]-bound[0])*w
    I = 0
    for i in range(N):
        I += w_map[i] * f(X_map[i],k)
    return I

