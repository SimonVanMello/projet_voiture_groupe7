#!/usr/bin/env python3
#coding: utf-8

import RPi.GPIO as GPIO
import time

class Ultrasonic:
    def __init__(self, triggerPin: int, echoPin: int):
        GPIO.setmode(GPIO.BOARD)
        self.GPIO_TRIGGER = triggerPin
        self.GPIO_ECHO = echoPin
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def getDistance(self) -> float:
        # Envoie une impulsion sur la broche TRIGGER
        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        # Calcul du temps de réponse
        pulse_start = time.time()
        while GPIO.input(self.GPIO_ECHO) == 0:
            pulse_start = time.time()

        pulse_end = time.time()
        while GPIO.input(self.GPIO_ECHO) == 1:
            pulse_end = time.time()

        # Calcule la distance en cm
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
    return distance

    def run(self):
        try:
            while True:
                distance = self.getDistance() 
                print(f"Distance: {distance} cm")
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()