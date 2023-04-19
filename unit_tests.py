#!/usr/bin/env python3
#coding: utf-8

import pytest
from sensors.Ultrasonic import Ultrasonic

class TestUltrasonic:
    def test_distance_left(self):
        leftSensor = Ultrasonic(23, 21)
        distance = leftSensor.getDistance()
        assert distance == 10
        
    def test_distance_right(self):
        rightSensor = Ultrasonic(37, 35)
        distance = rightSensor.getDistance()
        assert distance == 10
        
    def test_distance_front(self):
        frontSensor = Ultrasonic(31, 29)
        distance = frontSensor.getDistance()
        assert distance == 10

