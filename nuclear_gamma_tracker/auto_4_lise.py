"""Summary.


Primary file to be called on terminal. Will begin the process of finding information
for particular isotope. Run with the following command on terminal (from top-most directory): 

> python -m nuclear_gamma_tracker.auto_4_lise.py <isotope_start> <isotope_end> <wedge_start>
                           <wedge_end> <FP_width> -v  

Will prompt user to answer if LISE++ is running already with the GUI open. If not, 
answer "no" and it will locate the LISE++ image icon on your desktop and open it.
"""

from nuclear_gamma_tracker import implementation_4_auto as a4l
from nuclear_gamma_tracker import start_calls as strt
import sys 

def main():
    """Summary.

    Main function that prompts user if LISE++ GUI is open or not and calls
    the tuning function.
    """
    print("Beginning the automation for LISE++...")
    res = input("Are you opening the program for the first time? (yes or no): ")
    if res == "yes":
        FP_slit_width, isotope_start, isotope_end, wedge_range = strt.start()
    else:
        FP_slit_width, isotope_start, isotope_end, wedge_range = strt.start2()

    a4l.isotope_tuning_values(
        FP_slit_width,
        isotope_start,
        isotope_end,
        wedge_range)


if __name__ == "__main__":
    #print("ran as main on terminal")
    main()

main()