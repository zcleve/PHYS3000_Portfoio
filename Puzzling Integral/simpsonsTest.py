# Zackary Cleveland PHYS3000

import numpy as np


def f(z) :
    x = (z / (1 - z))
    dz = 1 / ((1 - z) ** 2)
    epsilon = 1e-10
    sin_x = np.sin(x)
    # From the joys of stack overflow and some gpt-shooting. For simpsons to work I need to take into account
    # scenarios where one could /0 or /close to zero or check for NAN values
    value = np.where(np.abs(x) > epsilon , sin_x / x , 1.0) * np.where(np.abs(x / 3) > epsilon ,
                                                                       np.sin(x / 3) / (x / 3) , 1.0) * np.where(
        np.abs(x / 5) > epsilon , np.sin(x / 5) / (x / 5) , 1.0) * dz
    return np.where(np.isfinite(value) , value , 0.0)


def simpsons(a , b , N) :
    h = (b - a) / N
    kodd = 0
    keven = 0

    for k in range(1 , N , 2) :
        kodd += f(a + (k * h))

    for k in range(2 , N , 2) :
        keven += f(a + (k * h))

    return (h / 3) * (f(a) + f(b) + 4 * kodd + 2 * keven)

N = 1000000
print('Error in', N, 'Steps:', simpsons(0 , .999999999 , N) - np.pi/2)

# Ideally, since this is exactly pi/2 the error would be smaller than what we are trying to detect with 7 terms.
# Since this is off by more than the -2.31e11 we are trying to find this methodology will not suffice
