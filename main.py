#!/usr/bin/env python3
#coding: utf-8

from motors.Dc import Dc
from motors.Servo import SensorAndMotor
from sensors.Ultrasonic import Ultrasonic
import time
import RPi.GPIO as GPIO

class Circle:
    def circleRight(self):
        try:
            servo = SensorAndMotor()
            servo.position = 425
            time.sleep(1)
            dc = Dc()
            dc.setup()
            dc.setSpeed(50)
            dc.forward()
            time.sleep(5)
            dc.stop()
            del servo
            del dc
            GPIO.cleanup()
        except Exception as e:
            print(e)
            dc.stop()

    def circleLeft(self):
        try:
            servo = SensorAndMotor()
            servo.position = 275
            time.sleep(1)
            dc = Dc()
            dc.setup()
            dc.setSpeed(50)
            dc.forward()
            time.sleep(4.7)
            dc.stop()
            del servo
            del dc
            GPIO.cleanup()
        except Exception as e:
            print(e)
            dc.stop()

    def run(self):
        self.circleRight()
        time.sleep(1)
        self.circleLeft()
        time.sleep(1)
        self.resetDirection()

    def resetDirection(self):
        servo = SensorAndMotor()
        servo.position = 350

class SensorFollower:
    def __init__(self):
        self.left_sensor = Ultrasonic(23, 21)
        self.front_sensor = Ultrasonic(31, 29)
        self.right_sensor = Ultrasonic(37, 35)
        self.servo = Servo(25, min_pulse_width=1.001/1000, max_pulse_width=2.0/1000, correction=0)

    def follow_sensor(self):
        while True:
            distance = self.front_sensor.distance * 100
            print('Distance en centimètre:', distance, 'cm')
            if 10 < distance < 20:
                self.servo.position_mid()
                print('Mid')
                sleep(0.1)
            elif distance < 10:
                self.servo.position_max()
                print('Tourne à gauche')
                sleep(0.1)
            elif distance > 20:
                self.servo.position_min()
                print('Tourne à droite')
                sleep(0.1)
sensorFollower = SensorFollower()
sensorFollower.follow_sensor()
#circle = Circle()
#circle.run()
