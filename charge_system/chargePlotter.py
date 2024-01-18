# Goals: plot the charges on an x-y grid and show the net forces as arrows
import netForcesChargeSystem as nfcs
import fileStripper as fs
import matplotlib.pyplot as plt
import numpy as np


def init_plot(path):
    charge_magnitudes, charge_positions = fs.read_magnitude_coordinate_format(path)
    charge_positions *= 100

    print(charge_positions)

    plt.style.use('_mpl-gallery')

    # Plot
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.scatter(charge_positions[0], charge_positions[1], charge_positions[2])

    ax.view_init(elev=20, azim=70)

    for i in range(0, charge_magnitudes.size):
        ax.text(charge_positions[i, 0], charge_positions[i, 1], charge_positions[i, 2], f'({charge_positions[i, 0]}, '
                                                                                        f'{charge_positions[i, 1]}, {charge_positions[i, 2]})',
                color='red')

    ax.set(xticklabels=[],
           yticklabels=[],
           zticklabels=[])

    ax.set_xlim(left=-2.5, right=6)
    ax.set_ylim(bottom=-1, top=2)
    ax.set_zlim(bottom=-1.5, top=3)

    plt.show()
