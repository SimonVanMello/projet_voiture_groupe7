import RPi.GPIO as GPIO
import time
import unittest

class moteurs(unittest.TestCase):
    def testArriere(self):
        print("Activation des moteurs")
        time.sleep(1)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)

        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)

        time.sleep(5)

        self.assertEqual(GPIO.input(17), GPIO.HIGH)
        print("Moteur gauche fonctionnel")

        self.assertEqual(GPIO.input(27), GPIO.HIGH)
        print("Moteur droit fonctionnel")

        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)

        time.sleep(1)
        GPIO.cleanup()

    def testAvant(self):

        print("Activation des moteurs")
        time.sleep(1)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)

        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)

        time.sleep(5)

        self.assertEqual(GPIO.input(18), GPIO.HIGH)
        print("Moteur droit fonctionnel")

        self.assertEqual(GPIO.input(22), GPIO.HIGH)
        print("Moteur droit fonctionnel")

        GPIO.output(18, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)

        time.sleep(1)
        GPIO.cleanup()

unittest.main()
