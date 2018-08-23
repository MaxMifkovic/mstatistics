"""
Statistics

Routines in this module:

mad(a)
"""

import numpy as np

def hello_world():
    return ("Hello, World!")

def mad(a):
    """
    Compute the mean absolute deviation of an array or matrix.

    Parameters
    ----------
    a : array_like
        Input array

    Returns
    -------
    out : float
        The mean absolute deviation.

    References
    ----------
    https://en.wikipedia.org/wiki/Average_absolute_deviation

    """

    out = np.mean(np.absolute(a - np.mean(a)))
    return out
