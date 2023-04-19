#!/usr/bin/env python3
#coding: utf-8

import RPi.GPIO as GPIO
import unittest
import time
from sensors.Ultrasonic import *

class Testultrasonic(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # this is the expected value in cm
        self.distance = 14
        super().setUpClass()

    def test_left_mesure(self):
        leftSensor = Ultrasonic(23,21)
        distance = leftSensor.getDistance()
        # self.assertEqual(distance, 20)
        borninf = self.distance - (self.distance/ 11.25)
        bornsup = self.distance + (self.distance/ 11.25)
        self.assertTrue(borninf <= distance <= bornsup)
        # if borninf <= self.distance <= bornsup:
        #     print("Distance correct")
        # else:
        #     print("Distance erronée")

    def test_front_mesure(self):
        frontSensor = Ultrasonic(31,29)
        distance = frontSensor.getDistance()
        # self.assertEqual(distance, 20)
        borninf = self.distance - (self.distance/ 11.25)
        bornsup = self.distance + (self.distance/ 11.25)
        self.assertTrue(borninf <= distance <= bornsup)
        # if borninf <= self.distance <= bornsup:        
        #     print("Distance correct")

        # else:
        #     print("Distance erronée")

    def test_right_mesure(self):
        rightSensor = Ultrasonic(37,35)
        distance = rightSensor.getDistance()
        # self.assertEqual(distance, 20)
        borninf = self.distance - (self.distance/ 11.25)
        bornsup = self.distance + (self.distance/ 11.25)
        self.assertTrue(borninf <= distance <= bornsup)
        # if borninf <= self.distance <= bornsup:
        #     print("Distance correct")
            
        # else:
        #     print("Distance erronée")

class TestInfra(unittest.TestCase):
    def test_infra(self):
        ir = Infra(20)
        result = ir.getInfo()
        self.assertEquals(1, result)

if __name__ == '__main__':
    unittest.main()