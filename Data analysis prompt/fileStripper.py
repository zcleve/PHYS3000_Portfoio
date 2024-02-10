# Zackary Cleveland PHYS3000
import numpy as np

#path = r'C:\Users\Zack\PycharmProjects\PHYS3000env\data\tensions.dat'

# this specific case is where the data can usefully be loaded into just a singular matrix
def get_data_matrix(path):
    return np.loadtxt(fname = path ,
                      dtype = 'float' ,
                      delimiter = '\t')