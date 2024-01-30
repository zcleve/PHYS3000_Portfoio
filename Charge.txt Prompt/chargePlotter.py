import netForcesChargeSystem as nfcs
import fileStripper as fs
import pyvista as pv


def init_plot(path) :
    # Strips the charge magnitudes and positions into variables from the txt file
    charge_magnitudes , charge_positions = fs.read_magnitude_coordinate_format(path)

    # Generates the vector that contains the net electric force on each particle
    nf_vector = nfcs.get_electric_net_force_matrix(charge_magnitudes , charge_positions)

    # Easier way to handle xyz coords of pts.
    points = pv.PointSet(charge_positions)

    # Defines plot object
    plot = pv.Plotter()

    # _ is the 'actor' for the plot. Things in the actors, or actors become visible on a plot when shown this
    # specifically adds the charges as points to our plot with their charge as the point 'magnitude' or scalar value
    _ = plot.add_points(
         points ,
         scalars = charge_magnitudes[:] ,
         render_points_as_spheres = True ,
         point_size = 30 ,
         show_scalar_bar = False
    )

    # Generates arrows with directions and magnitudes to represent and equate to the net electric force acting on the
    # Charged particles. Each arrow is scaled by 10^3 in order for it to be visible on the plot as the magnitudes for
    # Net electric forces are rather small as one would expect.
    _ = plot.add_arrows(
        charge_positions ,
        nf_vector ,
        10**3 ,
        show_scalar_bar = False
    )

    # Generates scalar bar/legend for the force arrow vectors.
    # The units are millinewtons as the arrows are scaled by 10^3
    _ = plot.add_scalar_bar(
        'Force Magnitude (millinewtons)' ,
        interactive = True ,
        vertical = True ,
        title_font_size = 25 ,
        label_font_size = 20 ,
        outline = False ,
        fmt = '%10.5f' ,
    )

    # Function name self-explanatory
    plot.add_axes_at_origin(
        x_color = None ,
        y_color = None ,
        z_color = None ,
        xlabel = 'X' ,
        ylabel = 'Y' ,
        zlabel = 'Z' ,
        line_width = 1 ,
        labels_off = True
    )
    # Attaches each magnitude to the corresponding point for display
    _ = plot.add_point_labels(
        charge_positions ,
        charge_magnitudes ,
        font_size = 20 ,
        point_size = 0 ,
        always_visible = True ,
        shadow = True ,
    )

    # Displays plot
    plot.show()
