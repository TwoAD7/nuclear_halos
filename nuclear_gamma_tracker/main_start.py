"""Summary.


Primary file to be called on terminal. Will begin the process of finding information
for particular isotope. Run with the following command on terminal (from top-most directory): 

> python -m nuclear_gamma_tracker.auto_4_lise.py  <isotope_start> <isotope_end> <wedge_start>
                           <wedge_end> <FP_width> -v  

Will prompt user to answer if LISE++ is running already with the GUI open. If not, 
answer "no" and it will locate the LISE++ image icon on your desktop and open it.
"""

from nuclear_gamma_tracker import implementation_file as a4l
import pyautogui as pag
import argparse as ap
import textwrap
import numpy as np
import time
import sys

#list of isotopes that are currently allowed 
isotopes = ['Mg_32','Mg_33','Mg_34','Mg_35','Mg_36','Mg_37','Mg_38','Mg_40']


#Here we create the parser
#the input for the parser comes from input given to auto_4_lise.py on terminal
p = ap.ArgumentParser(formatter_class=ap.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                Useful Information 
        ----------------------------------
             The range of Magnesium (Mg) isotopes that are currently 
             allowed are betwen Mg_32 - Mg_40 (excluding Mg_39).
             
             If no starting or ending Mg isotope is 
             specified, default values are:
             
             isotope_start='Mg_32'
             isotope_start='Mg_40'
             
             Enter the Focal Plane (FP) slit distance as an integer.
             This value is in milimeters.

             Two input values are required to specify the start and end 
             of the different values of the wedge thickness range. 

             The order of input to the parser goes as follows:

             If LISE++ is not open, place the '-f' to tell the parser it is the 'first time'

                -f isotope_start isotope_end wedge_range_start wedge_range_end FP_width -v

             If LISE++ is already open, place the '-nf' to tell the parser it is 'not the first time'
                -nf isotope_start isotope_end wedge_range_start wedge_range_end FP_width -v
             
         '''))
    
#Optional arguments
p.add_argument("-v","--verbose",action="store_true",help="Prints input from user in a verbose manner.")
p.add_argument("-f","--first_time",action="store_true",help="First time opening LISE++ optional argument",default=False)
p.add_argument("-nf","--not_first_time",action="store_true",help="Not first time opening LISE++ optional argument",default=False)

#Positional arguments 
p.add_argument("isotope_start",type=str,help="Isotope to begin with.",nargs="?",default="Mg_32",choices = isotopes)
p.add_argument("isotope_end",type=str,help="Isotope to end with.",nargs="?",default="Mg_40",choices = isotopes)
p.add_argument("wedge_range_start", type = int, help = "Starting value for wedge thickness at I2",
           nargs="?",default = 2300)
p.add_argument("wedge_range_end", type = int, help = "Ending value for wedge thickness at I2",
           nargs="?",default = 3100)
p.add_argument("FP_width", type = int, help = "Width for the Focal Plane (FP) in mm.",
           nargs="?",default = 10)

    #p.add_argument("echo", help= "prints out your input")

args = p.parse_args()

#If LISE++ is not open
if args.first_time:
    print("meow")
    _open = False

#If LISE++ is open already
if args.not_first_time:
    print("bark")
    _open = True

iso_start =  args.isotope_start
iso_end = args.isotope_end
wedge_start = args.wedge_range_start
wedge_end = args.wedge_range_end
FP_slit_width= args.FP_width

#if the '-v' is called on terminal
if args.verbose:
    print(f"Starting isotope: {args.isotope_start}\nEnding isotope: {args.isotope_end}\n")
    print(f"Starting wedge thickness: {args.wedge_range_start}\nEnding wedge thickness: {args.wedge_range_end}\n")
    print(f"The Focal Plane slit width is {FP_slit_width}")
else:
    print(f"{args.isotope_start}\n{args.isotope_end}")
    print(f"{args.wedge_range_start}\n{args.wedge_range_end}")
    print(f"{args.FP_width}")


def start_and_open():
    """Summary.

    Function to open LISE++ GUI from the icon logo that is on
    your desktop (very specific at the moment).
    """

    isotope_start = iso_start
    isotope_end = iso_end

    wedge_range_list = np.arange(int(wedge_start), int(wedge_end) +100,100)
    print(wedge_range_list)
    try:
        # find the image of the LISE++ icon,return coordinates for the cetner
        x, y = pag.center(pag.locateOnScreen("images/LISE++.png"))
        pag.moveTo(x, y)
    except TypeError:
        # if the app. has been clicked before
        x, y = pag.center(pag.locateOnScreen("images/LISE++_2.png"))
        pag.moveTo(x, y)
    pag.doubleClick()
    time.sleep(2.5)
    pag.moveTo(18, 44)  # file
    pag.doubleClick()
    pag.dragTo(112, 257, .5)  # configuration
    pag.click(interval=1)
    pag.moveTo(825, 251)  # load
    pag.click(interval=1)
    pag.moveTo(154, 326)  # textbox
    pag.click(interval=.5)
    pag.write("NSCL")
    pag.moveTo(471, 323)  # Open button
    pag.click()
    pag.moveTo(95, 213)  # A1900 file
    pag.click()
    pag.moveTo(471, 323)  # Open button
    pag.click()
    return FP_slit_width, isotope_start, isotope_end, wedge_range_list


def start_already_open():
    """Summary.

    If LISE++ GUI is already open and visible on your screen, this
    would be the start function that is to be used.
    """
    isotope_start = iso_start
    isotope_end = iso_end
    
    wedge_range_list = np.arange(int(wedge_start), int(wedge_end) +100,100)
    print(wedge_range_list)
    time.sleep(2.5)
    return FP_slit_width, isotope_start, isotope_end, wedge_range_list

def main(_open_):
    """Main function that calls all of the start functions"""

    if _open_:
        print("already opened!")
        FP_slit_width, isotope_start, isotope_end, wedge_range = start_already_open()
    else:
        print("not opened!")
        FP_slit_width, isotope_start, isotope_end, wedge_range = start_and_open()

    a4l.isotope_tuning_values(
        FP_slit_width,
        isotope_start,
        isotope_end,
        wedge_range)

if __name__ == "__main__":
    main(_open)

#main(_open)