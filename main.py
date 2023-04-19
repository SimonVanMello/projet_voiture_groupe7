#!/usr/bin/env python3
#coding: utf-8

from motors.Dc import Dc
from motors.Servo import SensorAndMotor
from sensors.Ultrasonic import Ultrasonic
import time
import RPi.GPIO as GPIO

class Circle:
    def circleRight(self):
        try:
            servo = SensorAndMotor()
            servo.position = 425
            time.sleep(1)
            dc = Dc()
            dc.setup()
            dc.setSpeed(50)
            dc.forward()
            time.sleep(5)
            dc.stop()
            del servo
            del dc
            GPIO.cleanup()
        except Exception as e:
            print(e)
            dc.stop()

    def circleLeft(self):
        try:
            servo = SensorAndMotor()
            servo.position = 275
            time.sleep(1)
            dc = Dc()
            dc.setup()
            dc.setSpeed(50)
            dc.forward()
            time.sleep(4.7)
            dc.stop()
            del servo
            del dc
            GPIO.cleanup()
        except Exception as e:
            print(e)
            dc.stop()

    def run(self):
        self.circleRight()
        time.sleep(1)
        self.circleLeft()
        time.sleep(1)
        self.resetDirection()

    def resetDirection(self):
        servo = SensorAndMotor()
        servo.position = 350

circle = Circle()
circle.run()