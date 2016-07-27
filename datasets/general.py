"""A module for generating toy data sets for generalized neural networks.

Generalized here simply refers to datasets that aren't specific to image
processing or natural language processing.
"""

import numpy as np

def gen_simple_linear(beta_0, beta_1, n_obs): 
    """Generate data that follows a univariate linear relationship.

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

def gen_multiple_linear(betas, n_obs): 
    """Generate data that follows a multivariate linear relationship. 
    
    This function assumes that the first `beta` in the `betas` corresponds
    to `beta_0`, and will associate a vector of 1's with this `beta`. 

    Args:
    ----
        betas: 1d np.ndarray of ints/floats
        n_obs: int

    Return:
    ------
        ys: 2d np.ndarray
        xs: 1d np.ndarray
    """
    
    n_vars = len(betas) - 1
    xs = np.random.random(size=(n_obs, n_vars))
    ones = np.ones(shape=(n_obs, 1))
    xs = np.concatenate([ones, xs], axis=1)

    ys = np.dot(xs, betas)

    return xs, ys
