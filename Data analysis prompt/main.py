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

import fileStripper as fs
import dataAnalysis as da
import dataPlotter as dp
import numpy as np

CORRECT_VALS = -np.linspace(11.0 , 16.5 , 56)

path = r'C:\Users\Zack\PycharmProjects\PHYS3000env\data\tensions.dat'

txt_file = fs.get_data_matrix(path)
mean = da.get_row_mean(txt_file)
stdev = da.get_row_stdev(txt_file)

dp.generate_x_correct_y_mean_y_error_as_stdv(CORRECT_VALS , mean , stdev)

# Answer to Q1, Q2, Q3:
# I would rate the software as decently effective. Examining just the raw data,
# it becomes pretty evident that the lower the tension value is, the greater
# the distribution of values within the expected one. The visualization reveals
# that the performance of the software is most limited in the low tension range.
# With the greatest standard deviations and general deviation from expected value
# occurring around -16,
