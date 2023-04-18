#!/usr/bin/env python3
#coding: utf-8

from motors.Servo import Servo
from random import randint
from sensors.Current import Current
import threading
from time import sleep

currentSensor = Current()
servo = Servo()

def runServo():
    for i in range(1, 11):
        position = randint(150, 650)
        print(f"Position {i}: {position}")
        # call the setter which will call the move method
        servo.position = position
        sleep(2)

def runCurrent():
    for i in range(20):
        current = round(currentSensor.checkCurrent(), 2)
        print(f"Courant: {current} mA")
        sleep(1)

threadServo = threading.Thread(target=runServo)
threadCurrent = threading.Current(target=runCurrent)

threadServo.start()
threadCurrent.start()