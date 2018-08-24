import pytest

from ..statistics import *

@requires('numpy')
def test_mad():
    assert mad(np.arange(1, 6)) - 6/5 <= 1e-5
