"""A module for activation functions"""

import numpy as np

def sigmoid(x):
    """Apply the sigmoid function to x"""

    return 1 / (1 + np.exp(-x))
