#Zackary Cleveland PHYS3000 - P1.B
#Units are in SI

v_initial = 8.0
x_initial = 10.0
x_accel = -3.0

# Kinematic equation for a change in X given a constant accel. and initial velocity and position.
# Runs in a while loop to return x values for all needed t values
t = .5

# Calculates and prints the position of the sprinter at the time intervals specified using a loop
while t <= 2.0:
    x_pos = x_initial + (v_initial * t) + (.5 * x_accel * t**2)
    print("At t =", t, "seconds, the sprinter is at x =", x_pos, "meters.")
    t = t + .5