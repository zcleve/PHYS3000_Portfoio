# Zackary Cleveland PHYS3000
# Goals:Task: First, let's visualize the data:
#
# For each row of the data, find the mean and standard deviation of those 30 data points.
# Make a plot of points where the  x  coordinate is the correct value of the parameter (so  −11.0  for the first row, and so on) and the  y  coordinate is the mean of the 30 data points.
# Add error bars to these points, where the size of each error bar is the corresponding standard deviation.
# Once you have your plots, answer the following questions:
#
# How would you qualify the performance of the software package? Did it do a good job or not?
# Are there regions where you would trust the software package and regions where you wouldn't? If so, why?
# If somebody were to use this software package to explore low tensions (parameters below  −16.5 ), what might you tell them?

import numpy as np
import matplotlib.pyplot as plt
# This code stops the printout using ellipsis to shorten
# import sys
# np.set_printoptions(threshold=sys.maxsize)

CORRECT_VALS = -np.linspace(11.0 , 16.5 , 56)

path = r'C:\Users\Zack\PycharmProjects\PHYS3000env\data\tensions.dat'
# def read_data_matrix(path):

txt_file = np.loadtxt(fname = path ,
                      dtype = 'float' ,
                      delimiter = '\t')

# to be used in the vector math or a new data analysis reusable library
def get_row_mean(matrix) :
    return np.mean(matrix, axis = 1)

# to be used in the vector math or a new data analysis reusable library
def get_row_stdev(matrix) :
    return np.std(matrix, axis = 1)

print(get_row_mean(txt_file))
print(get_row_stdev(txt_file))

plt.plot(CORRECT_VALS,get_row_mean(txt_file))
plt.errorbar(CORRECT_VALS,get_row_mean(txt_file), yerr = get_row_stdev(txt_file), xerr=None)
plt.show()