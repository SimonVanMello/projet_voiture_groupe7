import RPi.GPIO as GPIO
import time

class Infrarouge:
    def __init__(self, infr_pin):
        self.infr = infr_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.infr, GPIO.IN)
        time.sleep(0.1)

    def getInfo(self):
        etat = GPIO.input(self.infr)
        return etat

if __name__ == "__main__":
    infrarouge = Infrarouge(20)
    while True:
        print(infrarouge.getInfo())
        time.sleep(0.1)