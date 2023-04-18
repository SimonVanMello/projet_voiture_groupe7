#!/usr/bin/env python3
#coding: utf-8

from motors.Dc import Dc
from motors.Servo import SensorAndMotor
import threading

def circle():
    servo = SensorAndMotor()
    servo.position = 300
    dc = Dc()
    dc.setSpeed(20)
    threadServo = threading.Thread(target=servo.run)
    threadServo.start()
    try:
        while True:
            inp = input("1: change speed\n2: change angle\n> ")
            if inp == "stop":
                dc.stop()
                servo.position = 350
                break
            elif inp == "1":
                inp = int(input("New speed: "))
                dc.setSpeed(inp)
            elif inp == "2":
                inp = int(input("New angle: "))
                servo.position = inp
    except KeyboardInterrupt:
        dc.stop()
        servo.position = 350

circle()