#!/usr/bin/env python3
#coding: utf-8

import RPi.GPIO as GPIO
from time import sleep

class Infra:
    def __init__(self, infr_pin):
        self.infr = infr_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.infr, GPIO.IN)
        sleep(0.1)

    def getInfo(self):
        state = GPIO.input(self.infr)
        return state

if __name__ == "__main__":
    infra = Infra(20)
    try:
        while True:
            print(infra.getInfo())
            sleep(0.1)
    except KeyboardInterrupt:
        pass