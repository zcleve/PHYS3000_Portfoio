# Zackary Cleveland PHYS3000
import numpy as np

# returns the mean of a dataset across the rows as an array
def get_row_mean(matrix) :
    return np.mean(matrix, axis = 1)

# returns the standard deviation of a dataset across the rows as an array
def get_row_stdev(matrix) :
    return np.std(matrix, axis = 1)