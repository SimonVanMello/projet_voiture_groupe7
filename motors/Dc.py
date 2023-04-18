#!/usr/bin/env python3
#coding: utf-8

import board
import busio
import RPi.GPIO as GPIO
from Adafruit_PCA9685 import PCA9685
from time import sleep


class Dc:
    def __init__(self, pinEnable: int, pinIn1: int, pinIn2: int):
        self.pinEnable = pinEnable
        self.pinIn1 = pinIn1
        self.pinIn2 = pinIn2

        i2c = busio.I2C(board.SCL, board.SDA)
        self.__pwm = PCA9685(i2c)
        self.__pwm.set_pwm_freq(50)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pinIn1, GPIO.OUT)
        GPIO.setup(self.pinIn2, GPIO.OUT)

    def move(self, speed):
        self.__pwm.set_pwm(self.pinEnable, 0, speed)
        GPIO.output(self.pinIn1, GPIO.LOW)
        GPIO.output(self.pinIn2, GPIO.HIGH),222
        
    def stop(self):
        GPIO.output(self.pinIn1, GPIO.LOW)
        GPIO.output(self.pinIn2, GPIO.LOW)

dc = Dc(4, 15, 13)
dc.move(500)
sleep(4)
dc.stop()