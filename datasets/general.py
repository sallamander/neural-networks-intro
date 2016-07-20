"""A module for generating toy data sets for generalized neural networks.

Generalized here simply refers to datasets that aren't specific to image
processing or natural language processing.
"""

import numpy as np

def gen_simple_linear(beta_0, beta_1, n_obs): 
    """Generate data that follows a y = beta_0 + beta_1 * x_1 relationship.

    Args:
    ----
        beta_1: int/float
        beta_0: int/float
        n_obs: int

    Return:
    ------
        ys: 1d np.ndarray
        xs: 1d np.ndarray
    """
    
    xs = np.random.random(size=(n_obs, 1))
    ys = beta_0 + beta_1 * xs

    return xs, ys
