"""Summary.

Start calls to start the program. Will prompt user to answer if LISE++ is running
already with the GUI open. If not, answer "no" and it will locate the image
on your desktop and open it.
"""

from nuclear_gamma_tracker import automation_4_lise as a4l
import pyautogui as pag
import numpy as np
import time


def start():
    """Summary.

    Function to open LISE++ GUI from the icon logo that is on
    your desktop (very specific at the moment).

    """
    ans = input("Do you want to start from a particular isotope? (yes or no): ")
    if ans == "yes" or ans == "YES" or ans == "Yes":
        isotope_start = a4l._isotope_start()
    elif ans in ("no", "No", "NO"):
        isotope_start = "Mg_32"
        print(f"Starting with {isotope_start}...")
    else:
        input_flag = True
        while input_flag:
            ans = input(
                "Invalid input. Only 'yes' or 'no' accepted. Do you want to \
                start from a particular isotope? (yes or no): ")
            if ans == "yes":
                input_flag = False
                isotope_start = a4l._isotope_start()
                break
            elif ans == "no":
                input_flag = False
                isotope_start = "Mg_32"
                print(f"Starting with {isotope_start}...")
                break

    ans2 = input("Do you want to end with a particular isotope? (yes or no): ")
    if ans2 == "yes" or ans2 == "YES" or ans2 == "Yes":
        # flag = True
        isotope_end = a4l._isotope_end()
    elif ans2 == "no" or ans2 == "No" or ans2 == "NO":
        isotope_end = "Mg_40"
        print(f"Ending with {isotope_end}...")
    else:
        _input_flag = True
        while _input_flag:
            ans2 = input(
                "Invalid input. Only 'yes' or 'no' accepted. Do you want to \
                end from a particular isotope? (yes or no): ")
            if ans2 == "yes":
                _input_flag = False
                isotope_end = a4l._isotope_end()
                break
            elif ans2 == "no":
                _input_flag = False
                isotope_end = "Mg_40"
                print(f"Ending with {isotope_end}...")
                break

    FP_slit_width = input("Enter the width of the FP slits: ")
    wedge_range = input(
        "What is the min. and max. of your wedge selection? \
        ( 2300,3100 for example) ")
    # get rid of the underscore in the isotope name
    wedge_range = wedge_range.replace(",", " ")
    wedge_range = wedge_range.split()
    wedge_range_list = np.arange(
        int(wedge_range[0]), int(wedge_range[1]) + 100, 100)
    try:
        # find the image of the LISE++ icon,return coordinates for the cetner
        x, y = pag.center(pag.locateOnScreen("LISE++.png"))
        pag.moveTo(x, y)
    except TypeError:
        # if the app. has been clicked before
        x, y = pag.center(pag.locateOnScreen("LISE++_2.png"))
        pag.moveTo(x, y)
    pag.doubleClick()
    time.sleep(2.5)
    pag.moveTo(18, 44)  # file
    pag.doubleClick()
    pag.dragTo(112, 257, .5)  # configuration
    pag.click(interval=.5)
    pag.moveTo(825, 251)  # load
    pag.click(interval=.5)
    pag.moveTo(154, 326)  # textbox
    pag.click()
    pag.write("NSCL")
    pag.moveTo(471, 323)  # Open button
    pag.click()
    pag.moveTo(95, 213)  # A1900 file
    pag.click()
    pag.moveTo(471, 323)  # Open button
    pag.click()
    return FP_slit_width, isotope_start, isotope_end, wedge_range_list


def start2():
    """Summary.

    If LISE++ GUI is already open and visible on your screen, this
    would be the start function that is to be used.
    """
    ans = input("Do you want to start from a particular isotope? (yes or no): ")
    if ans == "yes" or ans == "YES" or ans == "Yes":
        isotope_start = a4l._isotope_start()
    elif ans == "no" or ans == "No" or ans == "NO":
        isotope_start = "Mg_32"
        print(f"Starting with {isotope_start}...")
    else:
        input_flag = True
        while input_flag:
            ans = input(
                "Invalid input. Only 'yes' or 'no' accepted. Do you want \
                to start from a particular isotope? (yes or no): ")
            if ans == "yes":
                input_flag = False
                isotope_start = a4l._isotope_start()
                break
            elif ans == "no":
                input_flag = False
                isotope_start = "Mg_32"
                print(f"Starting with {isotope_start}...")
                break

    ans2 = input("Do you want to end with a particular isotope? (yes or no): ")
    if ans2 == "yes" or ans2 == "YES" or ans2 == "Yes":
        # flag = True
        isotope_end = a4l._isotope_end()
    elif ans2 == "no" or ans2 == "No" or ans2 == "NO":
        isotope_end = "Mg_40"
        print(f"Ending with {isotope_end}...")
    else:
        _input_flag = True
        while _input_flag:
            ans2 = input(
                "Invalid input. Only 'yes' or 'no' accepted. Do you want to \
                end from a particular isotope? (yes or no): ")
            if ans2 == "yes":
                _input_flag = False
                isotope_end = a4l._isotope_end()
                break
            elif ans2 == "no":
                _input_flag = False
                isotope_end = "Mg_40"
                print(f"Ending with {isotope_end}...")
                break
    FP_slit_width = input("Enter the width of the FP slits: ")
    wedge_range = input(
        "What is the min. and max. of your wedge selection? ( 2300,3100 for example) ")
    # get rid of the underscore in the isotope name
    wedge_range = wedge_range.replace(",", " ")
    wedge_range = wedge_range.split()
    wedge_range_list = np.arange(
        int(wedge_range[0]), int(wedge_range[1]) + 100, 100)
    print(wedge_range_list)
    time.sleep(2.5)
    return FP_slit_width, isotope_start, isotope_end, wedge_range_list
