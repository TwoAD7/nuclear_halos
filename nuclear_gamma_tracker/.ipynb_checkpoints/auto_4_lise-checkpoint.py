"""Summary.

File to be called on terminal; will begin the process of finding specific information
for particular isotope
"""
import automation_4_lise as a4l
import start_calls as strt


def main():
    """Summary.

    Main function that prompts user if LISE++ GUI is open or not.
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
    main()
