#!/usr/bin/env python3
#coding: utf-8

from motors.Servo import Servo
from random import randint
from time import sleep

servo = Servo()
# test the motor with 10 random positions
for i in range(1, 11):
    position = randint(150, 650)
    print(f"Position {i}: {position}")
    # call the setter which will call the move method
    servo.position = position
    sleep(2)