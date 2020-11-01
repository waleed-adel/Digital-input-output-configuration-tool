# Digital input output configuration tool
 ## DIO Configuration Tool
 ### Main Idea
 - Each embedded system project has its own configuration for its drivers.
 For ex. DIO, TIMERS and Communication drivers.
 - In this project, The target is to make a GUI configuration tool for
 DIO to generate its configuration files instead of manually
 editing the existing files.

 ### Requirements:
 - The tool shall be able to configure all the micro-controller
 pins.
 - Each pin shall have the following configurations
	- O/P with I.V = 0   ==> Output with initial value = 0
	- O/P with I.V = 1   ==> Output with initial value = 1
	- I/P with I.V = 0   ==> Intput with initial value = 0
	- I/P with I.V = 1   ==> Intput with initial value = 1
	- Note: Check the screen shot attached 
		and take it as a reference or a basic visualisation.
		file name: "Basic_PinConfig.PNG"
 - The tool shall have 3 buttons for configuration:
	- New -> create a file with any extension to save the current
	configurations.
	- Save -> to save the changes you made to the file.
	- Load -> to load a previous configurations.
	
  ### Output
  - DIO configurator generated a ".h" file that contains macros defining
    ports configuration.
  - Note: Check the file "PORT_config.h"
  	- Path: "Output_Examples/PORT_Config.h"
  - You can run the DIO configurator directly from "AVR_PortConfig.py"
  - You can easily change the GUI from "AVR_PortConfig.ui" 
    but then you will have to generate the "AVR_PortConfig.py" file again
    using the following command: pyside2-uic file_name.ui -o file_name.py
