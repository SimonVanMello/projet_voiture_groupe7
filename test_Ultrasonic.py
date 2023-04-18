#!/usr/bin/env python3
#coding: utf-8

from sensors.Ultrasonic import Ultrasonic
from time import sleep

leftSensor = Ultrasonic(23, 21)
frontSensor = Ultrasonic(31, 29)
rightSensor = Ultrasonic(37, 35)

for i in range(10):
    leftSensorDistance = leftSensor.getDistance()
    frontSensorDistance = frontSensor.getDistance()
    rightSensorDistance = rightSensor.getDistance()
    print(f"Left: {leftSensorDistance} - Front: {frontSensorDistance} - Right: {rightSensorDistance}")
    sleep(1)