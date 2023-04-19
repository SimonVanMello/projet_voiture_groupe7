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

    def smoothCircle(self):
        servo = SensorAndMotor()
        changePosition(servo, 275, 0.01)
        dc = Dc()
        dc.setup()
        dc.setSpeed(50)
        dc.forward()
        time.sleep(4.7)
        changePosition(servo, 425, 0.01)
        time.sleep(5)
        dc.stop()
        del servo
        del dc
        GPIO.cleanup()
        
    def changePosition(self, servo: SensorAndMotor, newPos: int, delay: float):
        oldPosition = servo.position
        for i in range(oldPosition, newPos):
            servo.position = i
            time.sleep(delay)

    def run(self):
        self.circleRight()
        time.sleep(1)
        self.circleLeft()
        time.sleep(1)
        self.resetDirection()

    def resetDirection(self):
        servo = SensorAndMotor()
        servo.position = 350

#circle = Circle()
#circle.run()
#circle.smoothCircle()

class SensorFollower:
    def __init__(self):
        self.left_sensor = Ultrasonic(23, 21)
        self.front_sensor = Ultrasonic(31, 29)
        self.right_sensor = Ultrasonic(37, 35)
        self.servo = SensorAndMotor()
        self.dc = Dc()

    def follow_sensor(self):
        self.dc.setup()
        self.dc.setSpeed(30)
        self.dc.forward()
        try:
            while True:
                distance = self.left_sensor.getDistance()
                print('Distance en centimètre:', distance, 'cm')
                if 10 < distance < 20:
                    self.servo.positionMid()
                    print('Mid')
                    time.sleep(0.1)
                elif distance < 10:
                    self.servo.positionMax()
                    print('Tourne à droite')
                    time.sleep(0.1)
                elif distance > 20:
                    self.servo.positionMin()
                    print('Tourne à gauche')
                    time.sleep(0.1)
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.dc.stop()
            GPIO.cleanup()

sensorFollower = SensorFollower()
sensorFollower.follow_sensor()