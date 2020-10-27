import sys
import pytest 
sys.path.append("..") # Adds higher directory to python modules path.
print(sys.path)
import automation4LISE as a4l


class Testautomation():

	def test_iso_start(self):
		"""Simple test to see if it retuns a string given a string."""
		out =  a4l._isotope_start("Mg_33")
		assert type(out) == str 

	def test_input1(self):
		a4l._isotope_start.input = lambda: "Mg_33"
		out = a4l._isotope_start()
		assert out == "Mg_33"

	def test_input2(self):
		a4l._isotope_start.input = lambda: "Mg_40"
		out = a4l._isotope_start()
		assert out == "Mg_40"

	"""def test_zero_division():
		with pytest.raises(ZeroDivisionError):
			1/0

	def test_exceptions(self):
		with pytest.raises(ValueError) as exc:
			#a4l._isotope_start.input = lambda: "Mg_33"
			out = a4l._isotope_start()
		#	a4l._isotope_start()
			#raise ValueError("Hey")
		assert exc.type == ValueError"""

	
#a4l.hi()