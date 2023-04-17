import RPi.GPIO as GPIO
import time

def callback_up(test):
    print("Détection %s" % test)

PIR = 34
GPIO.setmode(GPIO. BCM)
GPIO.setup(PIR, GPIO.IN)

try:
    GPIO.add_event_detect(PIR, GPIO.RISING, callback=callback_up)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    print("GPIO cleared")
    GPIO.cleanup()