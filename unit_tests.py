#!/usr/bin/env python3
#coding: utf-8

import RPi.GPIO as GPIO
import unittest
import time
from sensors.Ultrasonic import *

class Testultrasons(unittest.TestCase):
    def test_left_mesure(self):
        leftSensor = Ultrasonic(23,21)
        distance = leftSensor.getDistance()
        self.assertEqual(distance, 20)
        borninf = self.distance + (self.distance/ 11.25)
        bornsup = self.distance - (self.distance/ 11.25)

        if borninf <= self.distance <= bornsup:
            print("Distance correct")

        else:
            print("Distance erronée")

    def test_front_mesure(self):
        frontSensor = Ultrasonic(31,29)
        distance = frontSensor.getDistance()
        self.assertEqual(distance, 20)
        borninf = self.distance + (self.distance/ 11.25)
        bornsup = self.distance - (self.distance/ 11.25)

        if borninf <= self.distance <= bornsup:        
            print("Distance correct")

        else:
            print("Distance erronée")

    def test_right_mesure(self):
        rightSensor = Ultrasonic(37,35)
        distance = rightSensor.getDistance()
        self.assertEqual(distance, 20)
        borninf = self.distance + (self.distance/ 11.25)
        bornsup = self.distance - (self.distance/ 11.25)

        if borninf <= self.distance <= bornsup:
            print("Distance correct")
            
        else:
            print("Distance erronée")

if __name__ == '__main__':
    #unittest.main()
    pass