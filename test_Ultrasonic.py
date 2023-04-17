#!/usr/bim/env python3
#coding: utf-8

from sensors.Ultrasonic import Ultrasonic

# test left sensor
leftSensor = Ultrasonic(23, 21)
leftSensorDistance = leftSensor.getDistance()
print(f"Left sensor value: {leftSensorDistance} cm")

# test front sensor
frontSensor = Ultrasonic(31, 29)
frontSensorDistance = frontSensor.getDistance()
print(f"Front sensor value: {frontSensorDistance} cm")

# test right sensor
rightSensor = Ultrasonic(37, 35)
rightSensorDistance = rightSensor.getDistance()
print(f"Right sensor value: {rightSensorDistance} cm")