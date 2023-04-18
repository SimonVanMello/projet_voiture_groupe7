import RPi.GPIO as GPIO
import time
def getInfo():
    infr = 20
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(infr, GPIO.IN)
    time.sleep(0.1)

    # Read the sensor data
    etat = GPIO.input(infr)
    return etat

while True:
    print(getInfo())