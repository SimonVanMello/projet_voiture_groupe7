#!/usr/bin/env python3
#coding: utf-8

import RPi.GPIO as GPIO
from time import sleep


class Dc:
    def __init__(self, pinEnable: int, pinIn1: int, pinIn):
        self.__pwm = Adafruit_PCA9685.PCA9685()
        self.__pwm.set_pwm_freq(60)
        self.__position  = 200

    def move(self):
        self.__pwm.set_pwm(4, 0, self.__position)

dc = Dc()
dc.move()