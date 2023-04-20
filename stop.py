#!/usr/bin/env python3
#coding: utf-8

from motors.Dc import Dc
from motors.Servo import SensorAndMotor
import time
import RPi.GPIO as GPIO

dc = Dc()
dc.setup()
dc.setSpeed(0)
dc.stop()
del dc

servo = SensorAndMotor()
servo.position = 350
del servo

GPIO.cleanup()