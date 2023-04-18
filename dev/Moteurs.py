import RPi.GPIO as GPIO
import Adafruit_PCA9585
import time

GPIO.setmode(GPIO.BOARD)
mot1 = 11
mot2 = 12
GPIO.setup(mot1, GPIO.OUT)
GPIO.setut(mot2, GPIO.OUT)

GPIO.output(mot1, GPIO.HIGH)
GPIO.output(mot2, GPIO.LOW)
time.sleep(5)

# Arrêter les moteurs
GPIO.output(mot1, GPIO.LOW)
GPIO.output(mot2, GPIO.LOW)

# Nettoyer les broches GPIO
GPIO.cleanup()