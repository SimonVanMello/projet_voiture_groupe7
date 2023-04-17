#!/usr/bim/env python3
#coding: utf-8

from motors.Servo import Servo
from random import randint
from time import sleep

servo = Servo()
for i in range(1, 11):
    position = randint(150, 650)
    print(f"Position {i}: {position}")
    servo.move(position)
    sleep(2)