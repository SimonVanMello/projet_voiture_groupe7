
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
infr = 34
GPIO.setup(infr, GPIO.IN)

try:
    while 0:
        print("Ligne détectée")
except KeyboardInterrupt:
    print("Ligne perdue")
finally:
    GPIO.cleanup()