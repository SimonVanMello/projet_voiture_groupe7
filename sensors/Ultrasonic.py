#!/usr/bin/env python3
#coding: utf-8

import RPi.GPIO as GPIO
import time

class Ultrasonic:
    def __init__(self, triggerPin: int, echoPin: int):
        GPIO.setmode(GPIO.BCM)
        self.GPIO_TRIGGER = triggerPin
        self.GPIO_ECHO = echoPin
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def getDistance(self) -> float:
        # send a pusle on trigger pin
        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        # find response time
        pulse_start = time.time()
        while GPIO.input(self.GPIO_ECHO) == 0:
            pulse_start = time.time()

        pulse_end = time.time()
        while GPIO.input(self.GPIO_ECHO) == 1:
            pulse_end = time.time()

        # get distance in cm
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance

    def run(self):
        try:
            while True:
                distance = self.getDistance() 
                print(f"Distance: {distance} cm")
                sleep(0.01)
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()

if __name__ == "__main__":
    leftSensor = Ultrasonic(11, 9) # board pins : 23 21
    frontSensor = Ultrasonic(6, 5) # board pins : 31 29
    rightSensor = Ultrasonic(26, 19) # board pins : 37 35

    for i in range(10):
        leftSensorDistance = leftSensor.getDistance()
        frontSensorDistance = frontSensor.getDistance()
        rightSensorDistance = rightSensor.getDistance()
        print(f"Left: {leftSensorDistance} - Front: {frontSensorDistance} - Right: {rightSensorDistance}")
        time.sleep(1)