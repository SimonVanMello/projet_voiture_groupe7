import RPi.GPIO as GPIO
import PCA9685 as p
import time


class vitesse:    
    def __init__(self, speed):
        self.speed = speed

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        if type(value) == int:
            self.__speed = value
        else:
            print("Mauvais type")

    def setSpeed(self):
        self.__speed = int(input("Quelle vitesse souhaitez vous choisir ?"))
        self.__speed *= 40
        pwm.write(METTRE CHANNEL 1, 0, speed)
        pwm.write(METTRE CHANNEL 2, 0, speed)

def setup(busnum=None):
	global forward0, forward1, backward1, backward0
	global pwm
	if busnum == None:
		pwm = p.PWM()                  
	else:
		pwm = p.PWM(bus_number=busnum)

	pwm.frequency = 60
	forward0 = 'True'
	forward1 = 'True'
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)  
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
	for pin in LISTE AVEC LES PINS:
		GPIO.setup(pin, GPIO.OUT)