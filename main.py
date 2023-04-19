#!/usr/bin/env python3
#coding: utf-8

from motors.Dc import Dc
from motors.Servo import SensorAndMotor
import threading

def circle():
    servo = SensorAndMotor()
    dc = Dc()
    dc.setup()
    dc.setSpeed(40)
    
    try:
        servo.position = 275

    except:
        dc.stop()
        servo.position = 350
circle()