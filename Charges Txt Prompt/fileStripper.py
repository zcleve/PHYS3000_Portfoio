import numpy as np

# given the path to a .txt file in the format of:
# magnitude_1 x_1 y_1 z_1
# magnitude_2 x_2 y_2 z_2
# ...
# Returns np array of the magnitudes and one of the positions of each row entry
def read_magnitude_coordinate_format(path):
    txt_file = np.loadtxt(fname=path,
                          dtype='float',
                          delimiter=' ')

    num_rows, num_columns = txt_file.shape

    magnitudes = np.array(txt_file[:, 0])
    position_matrix = np.array(txt_file[:, 1:num_rows - 1])
    return magnitudes, position_matrix
