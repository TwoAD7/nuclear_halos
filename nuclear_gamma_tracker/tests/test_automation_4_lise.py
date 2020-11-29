"""Summary.

This file is meant to run some basic tests on functions found in
'automation_4_lise.py' to assure it is running smoothly.
"""

import numpy as np
from nuclear_gamma_tracker import implementation_file as a4l
import pytest
#import sys
# sys.path.append("..")  # Adds higher directory to python modules path.
# print(sys.path)

#NEED TO ADD MORE TESTS

"""
def test_iso_start():
    #Simple test to see if it retuns a string given a string.
    out = a4l._isotope_start("Mg_33")
    assert isinstance(out, str)
"""

def test_arrayslicer():
    """Checking if slice function is still returning array with dictionaries (maps)."""
    isotope_info = [
        {"isotope": "Mg_32", "data": 0.0},
        {"isotope": "Mg_33", "data": 0.0},
        {"isotope": "Mg_34", "data": 0.0},
        {"isotope": "Mg_35", "data": 0.0},
        {"isotope": "Mg_36", "data": 0.0}, 
        ]
    out_array = [
        {"isotope": "Mg_34", "data": 0.0},
        {"isotope": "Mg_35", "data": 0.0},
        {"isotope": "Mg_36", "data": 0.0}, 
        ]
    sliced_array = a4l.slice_array(isotope_info, "Mg_34")
    assert np.array_equal(sliced_array, out_array)