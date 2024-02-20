import matplotlib.pyplot as plt


# takes two functions of time and plots them on the same plot for comparison with labels differing colors
def plot_input_vs_output_xy(t_space, fout, fin, title, label_in="Input", label_out="Output", color_in="magenta",
                            color_out="green", x_label="Time (t)", y_label="Output function f(t)"):
    fig, ax = plt.subplots()
    ax.plot(t_space, fout, color_out, label_out)
    ax.plot(t_space, fin, color_in, label_in)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.title(title)
    return ax

def plot_versus_time(t_space, x_space, title, label_f = "f(t)", color="red", x_label="Time (t)", y_label="f(t)" ):
    fig, ax = plt.subplots()

    ax.plot(t_space , x_space , color = color , label = label_f)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend()
    ax.set_title(title)
    ax.grid(True)

    return ax