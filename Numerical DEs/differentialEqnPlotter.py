import matplotlib.pyplot as plt


# say you have a 1st order ODE like a low pass filter, where the Vin is a signal as a f(t)
# takes inputs for fout and fin as 1d arrays
def plot_input_vs_output_xy(t_space, fout, fin, label_in="Input", label_out="Output", color_in="magenta",
                            color_out="green", x_label="Time (t)", y_label="Output function f(t)"):
    fig, ax = plt.subplots()
    ax.plot(t_space, fout, color_out, label_out)
    ax.plot(t_space, fin, color_in, label_in)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    return ax
