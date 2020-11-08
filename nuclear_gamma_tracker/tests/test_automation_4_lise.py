"""Summary.

This file is meant to run some basic tests on functions found in
'automation_4_lise.py' to assure it is running smoothly.
"""

import numpy as np
from nuclear_gamma_tracker import automation_4_lise as a4l
#import pytest
#import sys
# sys.path.append("..")  # Adds higher directory to python modules path.
# print(sys.path)


class Testautomation():

    def test_iso_start(self):
        """Simple test to see if it retuns a string given a string."""
        print(
            "Please enter Mg_33 when prompted for isotope. Checking if it retursn \
			the correc type.")
        out = a4l._isotope_start("Mg_33")
        assert isinstance(out, str)

    def test_input1(self):
        print("Please enter Mg_33 when prompted for isotope.")
        a4l._isotope_start.input = lambda: "Mg_33"
        out = a4l._isotope_start()
        assert out == "Mg_33"

    def test_input2(self):
        print("Please enter Mg_40 when prompted for isotope.")
        a4l._isotope_start.input = lambda: "Mg_40"
        out = a4l._isotope_start()
        assert out == "Mg_40"

    def test_arrayslicer(self):
        """Summary

        Checking if slice function is still returning array with dictionaries (maps).

        """
        isotope_info = [
            {"isotope": "Mg_32", "data": 0.0},
            {"isotope": "Mg_33", "data": 0.0},
            {"isotope": "Mg_34", "data": 0.0},
            {"isotope": "Mg_35", "data": 0.0},
            {"isotope": "Mg_36", "data": 0.0}, ]
        out_array = [
            {"isotope": "Mg_34", "data": 0.0},
            {"isotope": "Mg_35", "data": 0.0},
            {"isotope": "Mg_36", "data": 0.0}, ]

        sliced_array = a4l.slice_array(isotope_info, "Mg_34")
        assert np.array_equal(sliced_array, out_array)

    """def test_zero_division():
		with pytest.raises(ZeroDivisionError):
			1/0

	NEED TO WORK ON CHECKING EXCEPTIONS
	def test_exceptions(self):
		with pytest.raises(ValueError) as exc:
			#a4l._isotope_start.input = lambda: "Mg_33"
			out = a4l._isotope_start()
		#	a4l._isotope_start()
			#raise ValueError("Hey")
		assert exc.type == ValueError"""


# a4l.hi()
