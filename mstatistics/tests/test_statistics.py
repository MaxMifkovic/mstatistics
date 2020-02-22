import os, sys
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, path)

import pytest
import numpy as np

#from mstatistics import statistics
if __name__ == '__main__':
    import statistics
else:
    from . import statistics

def test_mad():
    """
    Test the mad() method for calculating mean absolute deviation.

    """
    assert statistics.mad(np.arange(1, 6)) - 6/5 <= 1e-5
    assert statistics.mad(np.arange(1, 6)) == 6/5
    assert statistics.mad([1, 2, 3, 4, 5]) == 6/5

def test_gaussian():
    """
    Test the gaussian() method for constructing a Gaussian distribution

    """
    assert np.argmax(statistics.gaussian(np.linspace(-100, 100, 101))) == 50

def test_cdf():
    """
    Test the cdf() method for creating a cummulative distribution function

    """
    assert statistics.cdf(np.arange(1, 11), normalize=False)[-1] == 10/2*(10 + 1)
    assert statistics.cdf(np.arange(1, 11), normalize=True)[-1] == 1

def test_nearest_index():
    """
    Test the nearest_index() method for finding the nearest index of a list or
    an array to a given value

    """
    assert statistics.nearest_index(np.arange(0, 5), -1) == 0
    assert statistics.nearest_index(np.arange(0, 5), 0) == 0
    assert statistics.nearest_index(np.arange(0, 5), 5) == 4
    assert statistics.nearest_index(np.arange(0, 5), 4) == 4

def test_probability():
    """
    Test the probability() method to calculate the probability of a region in a distribution

    """
    a = np.linspace(-100, 100, 101)
    b = statistics.gaussian(a)
    assert statistics.probability(a, b) == 1

def test_covariance():
    """
    Test the covariance method() for calcuting the covariance of a list of vectors

    """
    assert np.all(statistics.covariance([np.arange(0, 5),
                              np.arange(0, 5)]) == 2*np.ones([2, 2]))
    assert np.all(statistics.covariance(np.array([np.arange(0, 5),
                                       np.arange(0, 5)])) == 2*np.ones([2, 2]))
    assert np.all(statistics.covariance([np.arange(0, 5),
                              -1*np.arange(0, 5)]) == np.array([[2, -2],
                                                                [-2, 2]]))

def test_correlation():
    assert np.allclose(statistics.correlation([np.arange(0, 5),
                                    np.arange(0, 5)]), np.ones([2, 2]))
    assert np.allclose(statistics.correlation(np.array([np.arange(0, 5),
                                             np.arange(0, 5)])), \
                       np.ones([2, 2]))
    assert np.allclose(statistics.correlation([np.arange(0, 5),
                                    -1*np.arange(0, 5)]), \
                       np.array([[1, -1], [-1, 1]]))

if __name__ == "__main__":
    test_mad()
    test_gaussian()
    test_cdf()
    test_probability()
    test_nearest_index()
    test_covariance()
    test_correlation()