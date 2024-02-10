# Zackary Cleveland PHYS3000
import numpy as np
import gaussTest as gt
import borwein as bor
import time

# We have transformed x -> (z / (1 - z)) to handle the improper integral so bounds are [0,1]
bounds = [0, 1]
bor_residual = bor.bor_expected(8)
bor_7_or_less = bor.bor_expected(1)
print("First, lets find a minimum N to see that the Borwein of 7 to 1 terms is = pi/2")

delta = 1e-13
key = True
n = 1
k1 = 7
k2 = 8

while key:
    start = time.time()
    #print('For n =', n, 'our approximation is equal to, ', gt.gauss_legendre(bor.borwein, n, bounds))
    if np.abs(gt.gauss_legendre(bor.borwein, n, bounds, k1) - bor_7_or_less) <= (delta):
        print('For n =', n, 'we get the expected result of ', bor_7_or_less, 'or pi/2 to 13 decimal places')
        key = False
        end = time.time()
        print(end - start, 'seconds elapsed in calcualtion')
    else:
        print('For n =', n, 'we get a residual of', (gt.gauss_legendre(bor.borwein, n, bounds, k1) - bor_7_or_less), 'which is not close enough so we '
                                                                                 'increase N')
        n += 500
        end = time.time()
        print(end - start , 'seconds elapsed in calcualtion')

n_pi_by_2 = n

key = True

while key:
    start = time.time()
    if np.abs(gt.gauss_legendre(bor.borwein, n, bounds, k2) - bor_residual) <= (delta):
        print('For n =', n, 'we get the expected result of ', bor_residual, 'or about 467807924713440738696537864429 * pi / 935615849440640907310521750000 to 13 decimal places')
        key = False
    else:
        print('For n =', n, 'we get a residual of', gt.gauss_legendre(bor.borwein, n, bounds, k2) - bor_residual, 'which is not close enough so we '
                                                                                 'increase N')
        n += 5
        end = time.time()
        print(end - start , 'seconds elapsed in calcualtion')
n_residual = n

print("The takeaway from these calculations is the following: \nTo calculate borwein of n=7 where the expected result is pi/2 within 13 decimal places."
      "\nWe needed N =", n_pi_by_2, "in order to get effectively pi/2 exactly using my method of gaussian quadrature."
                                  "\nTo prove that borwein of n=8 is not pi/2 to the 13th decimal places it took N =", n_residual)




