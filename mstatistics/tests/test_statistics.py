import pytest
import numpy as np

from ..statistics import *

def test_mad():
    assert mad(np.arange(1, 6)) - 6/5 <= 1e-5
    assert mad(np.arange(1, 6)) == 6/5
    assert mad([1, 2, 3, 4, 5]) == 6/5
