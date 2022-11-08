import matplotlib.pyplot as plt
import numpy as np
import math


def plot_values(xlabels, ylabels, xvalues, yvalues):
    # xpoints = np.array(xvalues)
    # ypoints = np.array(yvalues)

    # plt.plot(xpoints, ypoints)

    # plt.xlabel(xlabel)
    # plt.ylabel(ylabel)
    
    figure, axis = plt.subplots(2, 2)

    # For Sine Function
    # for i in range(len(xvalues)):
    #     xpoints = np.array(xvalues[i])
    #     ypoints = np.array(yvalues[i])
    #     axis[0, i].plot(xpoints, ypoints)
    #     axis[0, i].set_title("graph")
    #     # axis[0, 0].xlabel(xlabels[i])
    #     # axis[0, 0].ylabel(ylabels[i])

    xpoints = np.array(xvalues[0])
    ypoints = np.array(yvalues[0])
    axis[0, 1].plot(xpoints, ypoints)
    axis[0, 1].set_title("energie")
    xpoints = np.array(xvalues[1])
    ypoints = np.array(yvalues[1])
    axis[0, 0].plot(xpoints, ypoints)
    axis[0, 0].set_title("force")
    xpoints = np.array(xvalues[2])
    ypoints = np.array(yvalues[2])
    axis[1, 0].plot(xpoints, ypoints)
    axis[1, 0].set_title("speed")
    xpoints = np.array(xvalues[3])
    ypoints = np.array(yvalues[3])
    axis[1, 1].plot(xpoints, ypoints)
    axis[1, 1].set_title("height")

    plt.show()
