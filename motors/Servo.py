#!/usr/bim/env python3
#coding: utf-8

import Adafruit_PCA9685
# from future import division
from time import sleep

class Servo:
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)
        self.SERVO_MIN = 150
        self.SERVO_MAX = 600

    # def set_servo_pulse(self, channel ,pulse):
    #     pulse_length = 1000000
    #     pulse_length //= 60
    #     print('{0} us per period'.format(pulse_length))
    #     pulse_length //= 4096
    #     print('{0} us per bit'.format(pulse_length))
    #     pulse *= 1000
    #     pulse //= pulse_length
    #     pwm.set_pwm(channel, 0, pulse)

    def move(self, position: int):
        if position in range(self.SERVO_MIN, self.SERVO_MAX):
            self.pwm.set_pwm(0, 0, position)