#!/usr/bin/env python3
#coding: utf-8

import RPi.GPIO as GPIO
import unittest
import time
from sensors.Ultrasonic import Ultrasonic
from sensors.Infra import Infra

class TestUltrasonic(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # this is the expected value in cm
        self.distance = 14
        super().setUpClass()

    def test_left_mesure(self):
        leftSensor = Ultrasonic(11,9)
        distance = leftSensor.getDistance()
        print(f"Distance mesured: {distance}")
        # self.assertEqual(distance, 20)
        borninf = self.distance - (self.distance/ 11.25)
        bornsup = self.distance + (self.distance/ 11.25)
        self.assertTrue(borninf <= distance <= bornsup, f"left distance: {distance}")
        # if borninf <= self.distance <= bornsup:
        #     print("Distance correct")
        # else:
        #     print("Distance erronée")

    def test_front_mesure(self):
        frontSensor = Ultrasonic(6,5)
        distance = frontSensor.getDistance()
        print(f"Distance mesured: {distance}")
        # self.assertEqual(distance, 20)
        borninf = self.distance - (self.distance/ 11.25)
        bornsup = self.distance + (self.distance/ 11.25)
        self.assertTrue(borninf <= distance <= bornsup, f"front distance: {distance}")
        # if borninf <= self.distance <= bornsup:        
        #     print("Distance correct")

        # else:
        #     print("Distance erronée")

    def test_right_mesure(self):
        rightSensor = Ultrasonic(26, 19)
        distance = rightSensor.getDistance()
        print(f"Distance mesured: {distance}")
        # self.assertEqual(distance, 20)
        borninf = self.distance - (self.distance/ 11.25)
        bornsup = self.distance + (self.distance/ 11.25)
        self.assertTrue(borninf <= distance <= bornsup, f"right distance: {distance}")
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
    unittest.main(TestUltrasonic())