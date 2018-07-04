import RPi.GPIO as gpio
import time

'''
This module handles the stepper motor and related properties.

TODO: 
1.speed control
2.consider moving gpio config to one place

'''

class stepper_motor:

	def __init__(self):
		print("Stepper control instantiated")
		gpio.setmode(gpio.BOARD)

		'''  Should decide on the pin config . Removed the first arg for safety. Consider moving the gpio config to main loop '''
		gpio.setup(, gpio.OUT)
		gpio.setup(, gpio.OUT)
		gpio.setup(, gpio.OUT)
		gpio.setup(, gpio.OUT)


	
	def __del__(self):
		print("Stepper motor destructor called")	
	
	def drive_motor():
		gpio.output(7, True)
		gpio.output(11, True)
		gpio.output(13, True)
		gpio.output(15, False)
		time.sleep(0.5)
		
