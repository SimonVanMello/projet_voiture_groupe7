#!/usr/bin/env python3
#coding: utf-8

import RPi.GPIO as GPIO
from time import sleep

class Infra:
    def __init__(self, infr_pin: int):
        self.infr = infr_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.infr, GPIO.IN)
        self.lapNumber = 0
        self.lineDetected = 0

    def getInfo(self):
        state = GPIO.input(self.infr)
        return state
    
    def run(self):
        while True:
            currentValue = self.getInfo()
            if currentValue == 0:
                self.lineDetected = 0
            elif currentValue == 1:
                self.lineDetected += 1

            if self.lineDetected > 3:
                self.lapNumber += 1
                self.lineDetected = 0
                sleep(5)
            sleep(0.1)


if __name__ == "__main__":
    infra = Infra(20)
    try:
        while True:
            print(infra.getInfo())
            sleep(0.1)
    except KeyboardInterrupt:
        pass