from rungeKatta1ODEv1 import runge_kutta
import firstOrderODE_Functionsv1 as f_ode
from differentialEqnPlotterv1 import plot_versus_time
from matplotlib.pyplot import show

# Solve for the velocity (in the  y  direction) of a baseball falling from rest for both drag-free and with-drag
# models. Use  c=1.225⋅10−3N s2/m2  for the case with drag, and use  m=0.142kg  (MLB standard) for the mass of the
# baseball. Plot the baseball's velocity over 5 seconds after it's dropped. When does drag become significant? How
# much does drag affect the baseball's velocity at the end of this 5 seconds?

# PROFICIENCY: p2.e

# initial variable creation
drag_coeff = 1.225 * (10 ** -3)
m = 0.142
t_elapsed = 5
t_elapsed3 = 60
dt = 100000
v0 = 0
g = 9.81

# generation of arrays to contain the dt # of values of velocity and time. calls the runge_katta function which has
# the function for free fall w/ and w/o drag passed to it, alongside other relevant args
x_values , t_values = runge_kutta(f_ode.f_free_fall_drag , v0 , t_elapsed , args = (drag_coeff , m) , dt = dt)
x2_values , t2_values = runge_kutta(f_ode.f_free_fall , v0 , t_elapsed , args = (g ,) , dt = dt)
x3_values , t3_values = runge_kutta(f_ode.f_free_fall_drag , v0 , t_elapsed3 , args = (drag_coeff , m) , dt = dt)

# calls the plot generation function for a vale with respect to time for each required plot
plot_versus_time(t_values , x_values , "Velocity vs Time over 5 seconds w/ drag" , label_f = 'v(t)' ,
                 y_label = 'Velocity, v(t)')
plot_versus_time(t3_values , x3_values , "Velocity vs Time over 60 seconds w/ drag" , label_f = 'v(t)' ,
                 y_label = 'Velocity, v(t)')
plot_versus_time(t2_values , x2_values , "Velocity vs Time over 5 seconds w/o drag" , label_f = 'v(t)' ,
                 y_label = 'Velocity, v(t)')

print("Examining the graphs, it is clear that for small times, 2 seconds and prior, drag has a near negligible effect.")
print("Past 2 seconds, however, it is evident that drag starts to take effect, and there is even a 5 m/s discrepancy. "
      "between drag and no drag after 5 seconds")
print("In the plot over 60 seconds, the full effect of drag is revealed, that it limits the speed of a falling object "
      "at the speed where drag force cancels out gravitational force.")
show()
