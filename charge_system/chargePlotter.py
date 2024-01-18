# Goals: plot the charges on an x-y grid and show the net forces as arrows
import netForcesChargeSystem as nfcs
import fileStripper as fs
import numpy as np
import pyvista

def init_plot(path):
    charge_magnitudes, charge_positions = fs.read_magnitude_coordinate_format(path)
    print("this is new code")