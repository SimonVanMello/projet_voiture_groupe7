import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
infr = 20
GPIO.setup(infr, GPIO.IN)
etat = GPIO.input(infr)

try:
    while etat == 1:
        print("Ligne détectée")
except:
    while etat == 0:
        print("Ligne perdue")
finally:
    GPIO.cleanup()