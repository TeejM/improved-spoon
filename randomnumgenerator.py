
#Generates a random binary number and diplays via leds



import RPi.GPIO as GPIO         
from random import randint      

# function that defines the GPIO pins for the nine output LEDs
def setGPIO():
	# define the pins (change these if they are different)
	gpio = [26, 19, 13]


	#set them up as output pins
	for i in gpio:
		GPIO.setup(i, GPIO.OUT)

	return gpio

# function that randomly generates an 8-bit binary number
def setNum():
	# create an empty list to represent the bits
	num= []
	# generate eight random bits
	for i in range(0, 3):
		#append a random bit (0 or 1) to the end of the list
		num.append(randint(0, 1))

	return num

# function that displays the sum (by turning on the appropriate LEDs)
def display():
	for i in range (len(num)):
		# if the i-th bit is 1, then turn the i-th LED on
		if (num[i] == 1):
			GPIO.output(gpio[i], GPIO.HIGH)
		# otherwise, turn it off
		else:
			 GPIO.output(gpio[i], GPIO.LOW)

