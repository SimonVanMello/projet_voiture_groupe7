#!/usr/bim/env python3
#coding: utf-8

import Adafruit_PCA9685
# from future import division
from time import sleep

class Servo:
    def __init__(self):
        self.__pwm = Adafruit_PCA9685.PCA9685()
        self.__pwm.set_pwm_freq(60)
        self.__position  = 375
        self.__SERVO_MIN = 150
        self.__SERVO_MAX = 600

    # def set_servo_pulse(self, channel ,pulse):
    #     pulse_length = 1000000
    #     pulse_length //= 60
    #     print('{0} us per period'.format(pulse_length))
    #     pulse_length //= 4096
    #     print('{0} us per bit'.format(pulse_length))
    #     pulse *= 1000
    #     pulse //= pulse_length
    #     pwm.set_pwm(channel, 0, pulse)

    # getter function using property decorator
    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, newPosition: int):
        if newPosition in range(self.__SERVO_MIN, self.__SERVO_MAX):
            # whenever the position change with a valid value, we update
            # the actual position by calling self.__move()
            self.__position = newPosition
            self.__move()
        else:
            print("Invalid value")

    def __move(self):
        self.__pwm.set_pwm(0, 0, self.__position)