"""Utilities for plotting"""

import matplotlib.pyplot as plt
import numpy as np

def plot_errors(errors, show=False, title="Errors Over Time", 
        ylabel="Mean Squared Error", iterations=None):
    """Display a plot of the errors over time

    Args:
    ----
        errors: 1-dimensional iterable of errors
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
