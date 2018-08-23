"""
Statistics

Routines in this module:

mad(a)
"""

import numpy as np

def hello_world():
    return ("Hello, World!")

def mad(a):
    return np.mean(np.absolute(a - np.mean(a)))
