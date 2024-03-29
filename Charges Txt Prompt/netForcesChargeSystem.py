import numpy as np

import vectorMath as vm


# I will make a much better function to do this in vectorMath.py at some point
# A function to take any list or array of xyz and return distances and r_hats
# between them
def get_distance_matricies(pos_matrix):
    # Enables input of any pos_matrix size
    rows, columns = pos_matrix.shape

    # Placeholders for output
    out = np.zeros([rows, rows])
    r_hats = np.zeros([rows, rows, 3])

    for i in range(rows):

        # Selected becomes our "current pos"
        selected = pos_matrix[i, :]

        # We remove what we selected from the new_matrix
        new_matrix = pos_matrix[i + 1:, :]

        # Using simple vector math we find the distance between the selected pt and each remaining pt
        for j in range(new_matrix.shape[0]):
            out[j, i] = points_distance(selected, new_matrix[j, :])
            r_hats[j, i, :] = gen_rhat(selected, new_matrix[j, :])
            # print(r_hats)

    # This output matrix is column based. The first one contains the distance from charges 1-2, 1-3, ... 1-n charges.
    # The second containing the distance from 2-3, 2-4, ... 2-n... and so on and so forth for remaining columns.
    return out, r_hats

# Solves for coulombs law's magnitude given 2 charges and a distance
def coulombs_law_mag(q1, q2, r):
    # Coulomb's constant
    k = 8.99 * (10 ** 9)
    return (k * q1 * q2) * (1 / (r ** 2))

# Returns a matrix
def get_electric_net_force_matrix(mag, pos):
    dist, r_hats = get_distance_matricies(pos)

    # Easy access to the # of charges. The size of this array is directly from the number of rows in the
    # Data file provided, which represents the number of charges or elements.
    sz = mag.size

    # Placeholder output
    net_f_electric = np.zeros([sz, 3])

    # Outer loop cycles through columns of the distance matrix. More specifically, it denotes which of the n
    # Charges it is dealing with. "s1 - 1" is used to skip the column of all zeros, explained below
    for i in range(sz - 1):

        # This inner loops takes the charge selected by the outer loop and calculates the necessary forces between
        # It and relevant charges.
        for j in range(sz):

            # The way the distance matrix is designed, it will fill towards a column of all zeros, loosing a single
            # Entry each column. This is to prevent redundancy in that the distance 1 - 2 and 2 - 1 are the same.
            # All pairs like this are skipped, and this causes the disappearing entry behavior
            if dist[j, i] != 0:
                # Calculates and adds the electric force from the two charges to the charge net force vector at the
                # position corresponding to the charge selected by the outer loop
                # f_electric = (k * mag[i] * mag[j + 1]) / (dist[j, i] ** 2)
                net_f_electric[i, :] += coulombs_law_mag(mag[i], mag[j + 1], dist[j, i]) * r_hats[j, i, :]
                net_f_electric[j + 1, :] -= coulombs_law_mag(mag[i], mag[j + 1], dist[j, i]) * r_hats[j, i, :]
                # net_f_electric[i] = net_f_electric[i] + f_electric

                # Avoids unnecessary calculations and looping by resolving the complimentary (Newtons 3rd Law) force
                # net_f_electric[j + 1] = net_f_electric[j + 1] - f_electric

    # Output is in the form of a vector whose entries are row-based and corresponding to each charge/entry
    print(net_f_electric)
    return net_f_electric

# Returns p2p distance
def points_distance(pos1, pos2):

    # The magnitude of a vector constructed by (pos2 - pos1) is the linear distance between the two points
    return np.linalg.norm(pos2 - pos1)

# Returns unit vector between 2 pts
def gen_rhat(pos1, pos2):
    r_hat = pos2 - pos1
    return r_hat * (1 / np.linalg.norm(pos2 - pos1))

# Original printout/terminal  output
def simulate_coulombs_law(path):

    # Takes a file in the following format:
    # #### ### ### ###
    # #### ### ### ###
    # ...
    # And throws it into a matrix Where each row is a charge, and the columns are: Magnitude X-coord Y-coord Z-coord
    charges = np.loadtxt(fname=path,
                         dtype='float',
                         delimiter=' ')

    # Like mentioned, the number of rows denotes the number of charges
    num_rows, num_columns = charges.shape

    # Creates a vector from the first column of the data file
    charge_magnitudes = charges[:, 0]

    # Creates n x 3 matrix where n is the number of charges and the 3 columns are the last 3 columns of the data file
    position_matrix = charges[:, 1:num_rows - 1]

    # Converts the matrix of charge positions into their relevant distances between each other
    # dist_matrix = get_distance_matricies(position_matrix)

    # Placeholder matrix of the net electric force in order to limit function calls
    nf_matrix = get_electric_net_force_matrix(charge_magnitudes, position_matrix)

    for i in range(0,num_rows):
        print("The net electric force on charge/entry no.", i, "is:", nf_matrix[i], "newtons")
    print("\n")


# Tester code
# simulate_coulombs_law('C:/Users/Zack/PycharmProjects/progressReport2/read_files/charge_list.txt')

# Example with modified entry
# simulate_coulombs_law('C:/Users/Zack/PycharmProjects/progressReport2/read_files/charge_list2.txt')
