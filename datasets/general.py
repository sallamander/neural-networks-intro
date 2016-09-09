"""A module for generating toy data sets for generalized neural networks.

Generalized here simply refers to datasets that aren't specific to image
processing or natural language processing.
"""

import numpy as np
from activations import sigmoid

def gen_simple_linear(beta_0, beta_1, n_obs): 
    """Return data that follows a univariate linear relationship.

    Args:
    ----
        beta_1: int/float
        beta_0: int/float
        n_obs: int

    Return:
    ------
        ys: 2d np.ndarray
        xs: 2d np.ndarray
    """
    
    xs = np.random.random(size=(n_obs, 1))
    ys = beta_0 + beta_1 * xs

    return xs, ys

def gen_multiple_linear(betas, n_obs): 
    """Return data that follows a multivariate linear relationship. 
    
    This function assumes that the first `beta` in the `betas` corresponds
    to `beta_0`, and will associate a vector of 1's with this `beta`. 

    Args:
    ----
        betas: 1d np.ndarray of ints/floats
        n_obs: int

    Return:
    ------
        ys: 2d np.ndarray
        xs: 2d np.ndarray
    """
    
    n_vars = len(betas) - 1
    xs = np.random.random(size=(n_obs, n_vars))
    ones = np.ones(shape=(n_obs, 1))
    xs = np.concatenate([ones, xs], axis=1)

    ys = np.dot(xs, betas)
    ys = ys.reshape(-1, 1)

    return xs, ys


def gen_multiple_logistic(betas, n_obs): 
    """Return data that follows a multivariate logistic function. 
    
    This function assumes that the first `beta` in the `betas` corresponds
    to `beta_0`, and will associate a vector of 1's with this `beta`. 

    Args:
    ----
        betas: 1d np.ndarray of ints/floats
        n_obs: int

    Return:
    ------
        ys: 2d np.ndarray
        xs: 2d np.ndarray
    """
    
    n_vars = len(betas) - 1
    # Scale data to get it centered at 0 (and not 0.5)
    xs = (np.random.random(size=(n_obs, n_vars)) - 0.5)
    ones = np.ones(shape=(n_obs, 1))
    xs = np.concatenate([ones, xs], axis=1)

    ys = 1 / (1 + np.exp(-np.dot(xs, betas)))
    ys = ys.reshape(-1, 1)

    return xs, ys

def gen_trigonometric(n_obs, func='sine'):
    """Return data that follows the sine or cosine function

    Args:
    ----
        n_obs: int
        func: str; possible values are 'sine', 'cosine', and 'tanh'

    Return:
    ------
        ys: 2d np.ndarray
        xs: 2d np.ndarray
    """

    xs = np.linspace(-3.14, 3.14, n_obs).reshape(-1, 1)

    if func == 'sine': 
        ys = np.sin(xs)
    elif func == 'cosine':
        ys = np.cos(xs)
    elif func == 'tanh':
        ys = np.tanh(xs)
    else:
        msg = "Must input 'sine', 'cosine', or 'tanh' for parameter `func`"
        raise ValueError(msg)
    
    ys = ys.reshape(-1, 1)

    return xs, ys

def gen_powx(n_obs, pow_x=2):
    """Return data that follows an x^`pow_x` relationship

    Args:
    ----
        n_obs: int
        pow_x: int

    Return:
    ------
        ys: 2d np.ndarray
        xs: 2d np.ndarray
    """

    xs = np.linspace(-5, 5, n_obs).reshape(-1, 1)
    ys = xs ** pow_x

    return xs, ys
