from nuclear_gamma_tracker import automation4LISE as a4l 
from nuclear_gamma_tracker import start_calls as strt 
import os 
#import platform

#interface to the automation script

def main():

	#Used to create the the "data.txt" and "pps_data.txt" prior to use.
	#home = os.path.expanduser('~') #find your home directory 
	"""
	desktop = home + "\Desktop"

	filename = desktop + "\data.txt"
	f = open(filename,"w")
	f.write("")
	f.close()

	_filename = desktop + "\pps_data.txt"
	g = open(_filename,"w")
	g.write("")
	g.close()
	"""
	
	
	print("Beginning the automation for LISE++...")
	res = input("Are you opening the program for the first time? (yes or no) ")
	if res == "yes":
		FP_slit_width,isotope_start,isotope_end,wedge_range=strt.start()  
	else:
		FP_slit_width,isotope_start,isotope_end,wedge_range=strt.start2()
	a4l.isotope_tuning_values(FP_slit_width,isotope_start,isotope_end,wedge_range)

if __name__ == "__main__":
    main()
