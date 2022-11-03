import matplotlib.pyplot as plt
import numpy as np

def plot_values(xlabel, ylabel, x_list, y_list):
    xpoints = np.array(x_list)
    ypoints = np.array(y_list)

    plt.plot(xpoints, ypoints)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()