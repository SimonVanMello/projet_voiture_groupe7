#!/usr/bin/env python3
#coding: utf-8

import RPi.GPIO as GPIO
import Adafruit_PCA9685
from time import sleep


class Dc:
    def __init__(self, pinEnable: int, pinIn1: int, pinIn2: int):
        self.pinEnable = pinEnable
        self.pinIn1 = pinIn1
        self.pinIn2 = pinIn2

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinIn1, GPIO.OUT)
        GPIO.setup(self.pinIn2, GPIO.OUT)

        self.__pwm = Adafruit_PCA9685.PCA9685()
        self.__pwm.set_pwm_freq(60)
        self.speed = 200
        self.__pwm.set_pwm(self.pinEnable, 0, self.speed)

    def move(self):
        GPIO.output(self.pinIn1, GPIO.LOW)
        GPIO.output(self.pinIn2, GPIO.HIGH)
        
    def stop(self):
        GPIO.output(self.pinIn1, GPIO.LOW)
        GPIO.output(self.pinIn2, GPIO.LOW)

dc = Dc(4, 15, 13)
dc.move()
sleep(4)
dc.stop()