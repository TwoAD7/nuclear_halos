def start():
	ans = input("Do you want to start from a particular isotope? (yes or no): ")
	if ans == "yes" or ans =="YES" or ans == "Yes":
		isotope_start= _isotope_start()
	elif ans == "no" or ans == "No" or ans == "NO":
		isotope_start = "Mg_32"
		print(f"Starting with {isotope_start}...")
	else:
		input_flag = True
		while input_flag:
			ans = input("Invalid input. Only 'yes' or 'no' accepted. Do you want to start from a particular isotope? (yes or no): ")
			if ans == "yes":
				input_flag = False
				isotope_start= _isotope_start()
				break
			elif ans =="no":
				input_flag = False
				isotope_start = "Mg_32"
				print(f"Starting with {isotope_start}...")
				break

	ans2 = input("Do you want to end with a particular isotope? (yes or no): ")
	if ans2 == "yes" or ans2 =="YES" or ans2 == "Yes":
		#flag = True
		isotope_end= _isotope_end()
	elif ans2 == "no" or ans2 == "No" or ans2 == "NO":
		isotope_end = "Mg_40"
		print(f"Ending with {isotope_end}...")
	else:
		_input_flag = True
		while _input_flag:
			ans2 = input("Invalid input. Only 'yes' or 'no' accepted. Do you want to end from a particular isotope? (yes or no): ")
			if ans2 == "yes":
				_input_flag = False
				isotope_end= _isotope_end()
				break
			elif ans2 =="no":
				_input_flag = False
				isotope_end = "Mg_40"
				print(f"Ending with {isotope_end}...")
				break

	FP_slit_width = input("Enter the width of the FP slits: ")
	wedge_range = input("What is the min. and max. of your wedge selection? ( 2300,3100 for example) ")
	wedge_range=wedge_range.replace(","," ") #get rid of the underscore in the isotope name
	wedge_range= wedge_range.split()
	wedge_range_list= np.arange(int(wedge_range[0]),int(wedge_range[1])+100,100)
	try:			
		x,y=pag.center(pag.locateOnScreen("LISE++.png"))# find the image of the LISE++ icon,return coordinates for the cetner 
		pag.moveTo(x,y)		
	except TypeError:
		x,y=pag.center(pag.locateOnScreen("LISE++_2.png"))	#if the app. has been clicked before 
		pag.moveTo(x,y)				
	pag.doubleClick()								
	time.sleep(2.5)
	pag.moveTo(18,44) #file
	pag.doubleClick()
	pag.dragTo(112, 257,.5) #configuration
	pag.click(interval=.5) 
	pag.moveTo(825,251) #load
	pag.click(interval=.5)
	pag.moveTo(154,326) #textbox
	pag.click()
	pag.write("NSCL")
	pag.moveTo(471,323) #Open button
	pag.click()
	pag.moveTo(95,213) #A1900 file 
	pag.click()
	pag.moveTo(471,323) #Open button
	pag.click()
	return FP_slit_width,isotope_start,isotope_end,wedge_range_list

#If the program is already open and GUI is viisible
def start2():
	ans = input("Do you want to start from a particular isotope? (yes or no): ")
	if ans == "yes" or ans =="YES" or ans == "Yes":
		isotope_start= _isotope_start()
	elif ans == "no" or ans == "No" or ans == "NO":
		isotope_start = "Mg_32"
		print(f"Starting with {isotope_start}...")
	else:
		input_flag = True
		while input_flag:
			ans = input("Invalid input. Only 'yes' or 'no' accepted. Do you want to start from a particular isotope? (yes or no): ")
			if ans == "yes":
				input_flag = False
				isotope_start= _isotope_start()
				break
			elif ans =="no":
				input_flag = False
				isotope_start = "Mg_32"
				print(f"Starting with {isotope_start}...")
				break

	ans2 = input("Do you want to end with a particular isotope? (yes or no): ")
	if ans2 == "yes" or ans2 =="YES" or ans2 == "Yes":
		#flag = True
		isotope_end= _isotope_end()
	elif ans2 == "no" or ans2 == "No" or ans2 == "NO":
		isotope_end = "Mg_40"
		print(f"Ending with {isotope_end}...")
	else:
		_input_flag = True
		while _input_flag:
			ans2 = input("Invalid input. Only 'yes' or 'no' accepted. Do you want to end from a particular isotope? (yes or no): ")
			if ans2 == "yes":
				_input_flag = False
				isotope_end= _isotope_end()
				break
			elif ans2 =="no":
				_input_flag = False
				isotope_end = "Mg_40"
				print(f"Ending with {isotope_end}...")
				break
	FP_slit_width = input("Enter the width of the FP slits: ")	
	wedge_range = input("What is the min. and max. of your wedge selection? ( 2300,3100 for example) ")
	wedge_range=wedge_range.replace(","," ") #get rid of the underscore in the isotope name
	wedge_range= wedge_range.split()
	wedge_range_list= np.arange(int(wedge_range[0]),int(wedge_range[1])+100,100)
	print(wedge_range_list)
	time.sleep(2.5)
	return FP_slit_width,isotope_start,isotope_end,wedge_range_list