import numpy as np


def read_magnitude_coordinate_format(path):
    txt_file = np.loadtxt(fname=path,
                          dtype='float',
                          delimiter=' ')

    num_rows, num_columns = txt_file.shape

    magnitudes = txt_file[:, 0]
    position_matrix = txt_file[:, 1:num_rows - 1]
    return magnitudes, position_matrix
