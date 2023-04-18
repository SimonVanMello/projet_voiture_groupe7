#!/usr/bin/env python3
#coding: utf-8

import adafruit_ina219
import board
import busio
import RPi.GPIO as GPIO
from time import sleep

class Current:
    def __init__(self):
        # Initialisation de la communication I2C avec le capteur INA219
        i2c = busio.I2C(board.SCL, board.SDA)
        self.ina219 = adafruit_ina219.INA219(i2c)

    def checkCurrent(self) -> float:
        current_mA = self.ina219.current
        return current_mA

    def run(self):
        while True:
            current = self.checkCurrent()
            print("Courant : %.2f mA" % current)
            sleep(1)