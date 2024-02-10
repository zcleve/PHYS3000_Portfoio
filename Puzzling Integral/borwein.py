# Zackary Cleveland PHYS3000
import numpy as np

def bor_expected(n):
    if n < 8:
        return(np.pi/2)
    elif n==8:
        return((467807924713440738696537864429 * np.pi) / 935615849440640907310521750000)
    else:
        return("Please enter n<=8")
def borwein(z, k) :
    x = (z / (1 - z))
    dz = 1 / ((1 - z) ** 2)
    f = 1
    for i in range(1,k+1):
        f*= np.sin(x / (2 * i - 1)) / (x / (2 * i - 1))
    return f * dz

