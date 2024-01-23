# Zackary Cleveland PHYS3000 P1.F
# Task: An induction motor consists of a square loop of coil,  20cm  by  20cm , rotating in a uniform magnetic field of strength  32mT.
#Calculate the magnetic flux through the coil when the angle between the coil and the field is
#θ=0  to  θ=π  in steps of  θ=π/8 , and print the flux value at each angle.

import math

# Defining needed variables to solve problem keeping in account given units of cm and mT
b_FieldMagnitude = 32 * (10 ** -3)
area_Magnitude = (20 * (10 ** -2)) ** 2
angle = 0

# Utilizes the algebraic equation for flux to calculate the flux at the specified angles in a loop
while angle <= math.pi:
    print("The Magnetic Flux in the coil at theta =", angle, "radians is:", "{:e}".format((b_FieldMagnitude * area_Magnitude * math.cos(angle))))
    angle = angle + math.pi/8



