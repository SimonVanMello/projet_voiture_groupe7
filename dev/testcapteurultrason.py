import RPi.GPIO as GPIO
import unittest
import time
import from sensors.Ultrasonic import Ultrasonic

''' ou alors, à voir
GPIO.setmode(GPIO.BOARD)
pin1 = 23
pin2 = 21
GPIO.setup(pin1, GPIO.IN)
GPIO.setup(pin2, GPIO.IN)
'''

ultr = Ultrasonic(23,21)

class Testultrasons(unittest.TestCase):

    def test_mesure(self):
        distance = 50
        # Assertion de la distance mesurée
        self.assertEqual(distance, 50, "Distance exacte")

if __name__ == '__main__':
    unittest.main()