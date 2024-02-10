# Zackary Cleveland PHYS3000

import matplotlib.pyplot as plt

def generate_x_correct_y_mean_y_error_as_stdv(vals, mean, stdev):
    plt.plot(vals,mean)
    plt.xlabel("Expected Tensions")
    plt.ylabel("Mean of Values Generated")
    plt.errorbar(vals,mean, yerr = stdev, xerr=None, label ='Standard Deviation')
    plt.legend(loc = 'lower right')
    plt.show()