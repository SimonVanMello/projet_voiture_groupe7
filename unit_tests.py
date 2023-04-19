#!/usr/bin/env python3
#coding: utf-8

import RPi.GPIO as GPIO
import unittest
import time
from sensors.Ultrasonic import *

''' ou alors, à voir
GPIO.setmode(GPIO.BOARD)
pin1 = 23
pin2 = 21
GPIO.setup(pin1, GPIO.IN)
GPIO.setup(pin2, GPIO.IN)
'''

class Testultrasons(unittest.TestCase):
    def test_left_mesure(self):
        leftSensor = Ultrasonic(23,21)
        distance = leftSensor.getDistance()
        self.assertEqual(distance, 20)

    def test_front_mesure(self):
        frontSensor = Ultrasonic(31,29)
        distance = frontSensor.getDistance()
        self.assertEqual(distance, 20)

    def test_right_mesure(self):
        rightSensor = Ultrasonic(37,35)
        distance = rightSensor.getDistance()
        self.assertEqual(distance, 20)

if __name__ == '__main__':
    unittest.main()