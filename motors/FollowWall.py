#!/usr/bin/env python
import RPi.GPIO as GPIO
import PCA9685 as p
from time import sleep   # Import necessary modules
import PCA9685 as servo
from sensors import Ultrasonic
from motors import Servo
from time import sleep
import time                  # Import necessary modules

MinPulse = 200
MaxPulse = 700

def setup2():
    global pwm
    pwm = servo.PWM()


def tourner():
    pwm.write(0, 0, 380)
    sleep(1)
    pwm.write(0, 0, 500)
    backward()
    sleep(0.9)
        



# ===========================================================================
# Raspberry Pi pin11, 12, 13 and 15 to realize the clockwise/counterclockwise
# rotation and forward and backward movements
# ===========================================================================
Motor0_A = 11  # pin11
Motor0_B = 12  # pin12
Motor1_A = 13  # pin13
Motor1_B = 15  # pin15

# ===========================================================================
# Set channel 4 and 5 of the servo driver IC to generate PWM, thus 
# controlling the speed of the car
# ===========================================================================
EN_M0    = 4  # servo driver IC CH4
EN_M1    = 5  # servo driver IC CH5

pins = [Motor0_A, Motor0_B, Motor1_A, Motor1_B]

# ===========================================================================
# Adjust the duty cycle of the square waves output from channel 4 and 5 of
# the servo driver IC, so as to control the speed of the car.
# ===========================================================================
def setSpeed(speed):
	speed *= 40
	print ('speed is: ', speed)
	pwm.write(EN_M0, 0, speed)
	pwm.write(EN_M1, 0, speed)

def setup(busnum=None):
	global forward0, forward1, backward1, backward0
	global pwm
	if busnum == None:
		pwm = p.PWM()                  # Initialize the servo controller.
	else:
		pwm = p.PWM(bus_number=busnum) # Initialize the servo controller.

	pwm.frequency = 60
	forward0 = 'True'
	forward1 = 'True'
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)        # Number GPIOs by its physical location
	try:
		for line in open("config"):
			if line[0:8] == "forward0":
				forward0 = line[11:-1]
			if line[0:8] == "forward1":
				forward1 = line[11:-1]
	except:
		pass
	if forward0 == 'True':
		backward0 = 'False'
	elif forward0 == 'False':
		backward0 = 'True'
	if forward1 == 'True':
		backward1 = 'False'
	elif forward1 == 'False':
		backward1 = 'True'
	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)   # Set all pins' mode as output

# ===========================================================================
# Control the DC motor to make it rotate clockwise, so the car will 
# move forward.
# ===========================================================================

def motor0(x):
	if x == 'True':
		GPIO.output(Motor0_A, GPIO.LOW)
		GPIO.output(Motor0_B, GPIO.HIGH)
	elif x == 'False':
		GPIO.output(Motor0_A, GPIO.HIGH)
		GPIO.output(Motor0_B, GPIO.LOW)
	else:
		print ('Config Error')

def motor1(x):
	if x == 'True':
		GPIO.output(Motor1_A, GPIO.LOW)
		GPIO.output(Motor1_B, GPIO.HIGH)
	elif x == 'False':
		GPIO.output(Motor1_A, GPIO.HIGH)
		GPIO.output(Motor1_B, GPIO.LOW)

def forward():
	motor0(forward0)
	motor1(forward1)

def backward():
    motor0(backward0)
    motor1(backward1)
    #pwm.write(0, 0, 380)
    #sleep(3)

def forwardWithSpeed(spd = 50):
	setSpeed(spd)
	motor0(forward0)
	motor1(forward1)

def backwardWithSpeed(spd = 50):
	setSpeed(spd)
	motor0(backward0)
	motor1(backward1)

def stop():
	for pin in pins:
		GPIO.output(pin, GPIO.LOW)

# ===========================================================================
# The first parameter(status) is to control the state of the car, to make it 
# stop or run. The parameter(direction) is to control the car's direction 
# (move forward or backward).
# ===========================================================================
def ctrl(status, direction=1):
	if status == 1:   # Run
		if direction == 1:     # Forward
			forward()
		elif direction == -1:  # Backward
			backward()
		else:
			print ('Argument error! direction must be 1 or -1.')
	elif status == 0: # Stop
		stop()
	else:
		print ('Argument error! status must be 0 or 1.')

#=========================================


sensor = Ultrasonic(23, 21)
leftSensor = Ultrasonic(23, 21)
frontSensor = Ultrasonic(31, 29)
rightSensor = Ultrasonic(37, 35)
#sensor2 = DistanceSensor(triggerpinGPIO, echopinGPIO)
myGPIO=25 
myCorrection=0
maxPW=(2.0+myCorrection)/1000
midPW=(0.75+myCorrection)/1000
minPW=(1.001-myCorrection)/1000
 
servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

while True:
    print('DIstance en centimètre', sensor.distance*100, 'cm')
    if (10 < sensor.distance*100 < 20 ):
        servo.positionMid()
        print("mid")
        sleep(0.1)
    if ( sensor.distance*100 < 10 ):
        servo.positionMax()
        print("tourne a gauche")
        sleep(0.1)

    if ( sensor.distance*100 > 20 ):
        servo.positionMin()
        print("tourne a droite")
        sleep(0.1)

#=========================================
def test():

	while True:
		setup()
		ctrl(1)
		time.sleep(3)
		setSpeed(10)
		forwardWithSpeed(10)
		backwardWithSpeed(10)
		time.sleep(3)
		setSpeed(100)
		forwardWithSpeed(100)
		backwardWithSpeed(100)
		time.sleep(3)
		ctrl(0)
		stop()

if __name__ == '__main__':
	setup()
	setup2()
	setSpeed(100)
	sleep(1)
	tourner()
	sleep(1)
	stop()
	pwm.write(0, 0, 380)