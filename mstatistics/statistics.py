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

def gaussian(a, mu=0, sigma=1):
    """
    Construct a Gaussian for a given range of values with a specified mean and
    standard deviation.

    Parameters
    ----------
    a : array_like
        Input array
    mu : float, optional
        Mean value of Gaussian
    sigma : float, optional
        Standard deviation of Gaussian

    Returns
    -------
    out : array_like
        Gaussian array corresponding to input array

    References
    ----------
    https://en.wikipedia.org/wiki/Normal_distribution

    https://www.maa.org/sites/default/files/pdf/upload_library/22/
    Allendoerfer/stahl96.pdf

    """

    out = np.exp(-1*(a - mu)**2 / (2*sigma**2)) / np.sqrt(2*np.pi*sigma**2)
    return out
