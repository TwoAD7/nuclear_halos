ABOUT THIS PACKAGE 
------------------

This package was created for the purpose of automating the tasks of finding yields for 
Magnesium isotopes between Mg 32 - Mg 40 with LISE++. It is meant to be ran after installing LISE++ 
on your computer. The target audience is meant to be members of the lifetime grout at 
NCSL/FRIB.
 * https://groups.nscl.msu.edu/lifetime/

However, anyone interested is also allowed to run this package. 

If you do not have LISE++ installed on your computer, you can go to the following link to install 
LISE++
 * http://lise.nscl.msu.edu/download/

For general information about LISE++, go to the following website
 * http://lise.nscl.msu.edu/lise.html

Follow the instructions that come with the installation of LISE++ to utilize this package. After LISE++ has been installed, make sure to have a shortcut (the logo) on your desktop as this package utilizes on finding the icon on your desktop. That is the way it is currently set up, later updates will work on ridding of the dependence on the icon to run the 
script.

Future updates will include the ability to use any isotope on the nuclear chart that LISE++ offers and update to the 
FRIB configuration as the Coupled Cyclotron Facility (CCF) was shutdow November 15th, 2020. 


INFORMATION ABOUT RUNNING SCRIPT:
----------------------------------

* Currently, only tested on Windows OS.

The automation scripts were written in python 3. If you do not have python 3 installed, you will need to install it as
certain functions are only available in python 3. A quick gooogle search on how to install python 3 for Windows will provide 
the information you need.

To check if you have python installed, go to your windows terminal and type:
 > python  

This should open python. If an error is invoked, you will need to install python 3. 

The following modules are required to run:
 - pyautogui 
 - matplotlib 
 - pyperclip
 - pandas
 - os 
 - platform 
 - time 
 - numpy 
 - sys 
 - textwrap 
 - argparse 

If they are not installed, they can be installed via the following command in your windows terminal:
 > pip install <MODULE> (example: pip install pyautogui)

If that does not work, try the following:
 > py -m pip install <MODULE> 

If you do not have pip installed, proceed to the following link to donwload pip:
  * https://phoenixnap.com/kb/install-pip-windows

<u>There are three files that are responsible for all of tasks regarding LISE++</u>
 - automation_4_lise.py 
 	- Implementation file containing all of functions that are called by  _start_calls.py_ and _auto_4_lise.py_
 - auto_4_lise.py
 	- The interface script that is responsible for starting the program. This is the function that is to be
 	called on terminal to begin te process. It is called with the following command on terminal:
 		- `python -m nuclear_gamma_tracker.auto_4_lise.py <isotope_start> <isotope_end> <wedge_start>  
 		<wedge_end> <FP_width> -v`
 			- Isotope start: Which Magnesium isotope you want to start with 
			- Isotope end  : Which Magnesium isotope you want to end with
			- Wedge start  : The starting wedge thickness at the I2 plane
			- Wedge end    : The terminating wedge thickness at the I2 plane
			- FP width     : The slit width of the focal plane slits at (used to control momentum acceptance of beam)

 - start_calls.py
 	- As the name implies, this script is meant to call the start functions that are found in _auto_4_lise.py_
 	- To view the contents of the parser in this script, and information about the 
 		positional arguments that are passed into _auto_4_lise.py_, run the following from the top-most directory 
 		- `python -m nuclear_gamma_tracker.start_calls.py -h`


DATA STORAGE 
------------

* The data is saved in individual .csv files for each corresponding Magnesium isotope in the same folder the scripts are in.
 It is then required from that the user visually inspects the .csv files to find best compromise between intensity and purity.

* The intermediate files "data.txt" and "pps_data.txt" are files that are created with the sole purpose of being reused. They are created when the script is originally executed and keeps being updated corresponding to each isotope. It is safe to delete these two files once you are done with the analysis. 

GENERAL INFORMATION
-------------------

* It is recommended to set all NSCL and FRIB files to have a momentum acceptance of 1% (dp/p = 1%) at the I2_Slits and the pre-separator focal plane (I4_PS_FP), respectively.

* To allow for largest intenisty possible on the FRIB/LISE++ configuration, the pre-separator 
slits (PS_Wedge_Slits) are set to the aperture limit, 135 mm. Wedges and momentum acceptances were 
later adjusted downstream to yield optimal purity results without large comprimise to intensity.

* FRIB intensities should be 2-3 orders of magnitude greater than NSCL intensities, roughly speaking.  

* If there are any errors/questions, please contact: salinas@frib.msu.edu
 

