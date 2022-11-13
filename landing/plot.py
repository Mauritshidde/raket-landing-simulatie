import matplotlib.pyplot as plt
import numpy as np


def plot_values(title, xlabel, ylabel, xvalues, yvalues):
    
    xpoints = np.array(xvalues)
    ypoints = np.array(yvalues)

    plt.plot(xpoints, ypoints)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
