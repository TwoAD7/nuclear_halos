from nuclear_gamma_tracker import automation4LISE as a4l

def test_iso_start():
	#a = "Cat"
	out =  a4l._isotope_start("Mg_33")
	#assert type(a)
	assert type(out) == str 
	
#a4l.hi()