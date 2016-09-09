"""Utilities for plotting"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def plot_errors(errors, show=False, title="Errors Over Time",
        ylabel="Mean Squared Error", iterations=None):
    """Display errors over time

    Args:
    ----
        errors: 1-dimensional iterable of errors
        show (optional): call `plt.show()`, to be used when not working in a
            notebook
        title (optional): str
        ylabel (optional): str
        iterations (optional): iterable with two ints, a beginning iteration
            and ending iteration
    """

    if iterations:
        beg, end = iterations[0], iterations[1]
        iteration_labels = np.arange(beg, end)
        errors = errors[beg:end]
    else:
        iteration_labels = np.arange(len(errors))
        beg, end = 0, len(errors)

    plt.plot(iteration_labels, errors, 'b-')
    plt.xlim(beg, end)
    plt.xlabel("Iteration")
    plt.ylabel(ylabel)
    plt.title(title)

def plot_func(xs, y_true, y_pred, func, n_nodes, font_size=10, show=False,
              ax=None, save_fp=None):
    """Display `xs`/`y_true` and `xs`/`y_pred` values for an inputted `func`

    Args:
    -----
        xs: 2d np.ndarray
        y_true: 2d np.ndarray
        y_pred: 2d np.ndarray
        func: str denoting what function the `xs`/`y_true` pairs follow
        n_nodes: number of nodes in hidden layer
        font_size (optional): Font size to use for plots
        show (optional): call `plt.show()`, to be used when not working in a
            notebook
        ax (optional): plt.Axes object to plot on
        save_fp (optional): filepath to save an image of the plot to
    """

    tit = '{} Function - {} Nodes in Hidden Layer'.format(func, n_nodes)

    font = {'size' : font_size}

    matplotlib.rc('font', **font)

    plot = plt if not ax else ax

    plot.plot(xs, y_true, 'r-', label='True Function')
    plot.plot(xs, y_pred, 'b-', label='Network Generated Function')


    y_min, y_max = y_true.min(), y_true.max()
    ylim_min = y_min - y_min * 0.1 if y_min >= 0 else y_min + y_min * 0.1
    ylim_max = y_max + y_max * 0.1
    if not ax:
        plot.title(tit)
        plot.xlabel('X Values')
        plot.ylabel('Y values')
        plot.ylim(ylim_min, ylim_max)
    else:
        plot.set_title(tit)
        plot.set_xlabel('X Values')
        plot.set_ylabel('Y values')
        plot.set_ylim(ylim_min, ylim_max)
    plot.legend(loc='best')

    if save_fp:
        plt.savefig(save_fp)
