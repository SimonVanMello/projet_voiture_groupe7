#!/usr/bim/env python3
#coding: utf-8

from sensors.Current import Current
from time import sleep

currentSensor = Current()
# check current voltage 10 times
for i in range(10):
    current = round(currentSensor.checkCurrent(), 2)
    print(f"Courant: {current} mA")
    sleep(1)