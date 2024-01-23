# Goals: plot the charges on an x-y grid and show the net forces as arrows
import netForcesChargeSystem as nfcs
import fileStripper as fs
import numpy as np
import pyvista as pv


def init_plot(path):
    charge_magnitudes, charge_positions = fs.read_magnitude_coordinate_format(path)
    nf_vector = nfcs.simulate_coulombs_law(path)

    plot = pv.Plotter()
    plot.add_points(charge_positions, scalars=charge_magnitudes[:], render_points_as_spheres=True, point_size=20)
    #charge_bar = plot.show_scalar_bar()
    #charge_bar.title = "Charge Magnitude"
    #plot.add_arrows(charge_positions, nf_vector)
    plot.show_bounds()
    plot.show()