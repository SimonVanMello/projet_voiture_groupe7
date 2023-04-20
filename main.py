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
        for i in range(oldPosition, newPos+1):
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
        self.left_sensor = Ultrasonic(11, 9)
        self.front_sensor = Ultrasonic(6, 5)
        self.right_sensor = Ultrasonic(26, 19)
        self.servo = SensorAndMotor()
        self.dc = Dc()

    def follow_sensor(self):
        self.dc.setup()
        self.dc.setSpeed(30)
        self.dc.forward()
        try:
            while True:
                left_distance = self.left_sensor.getDistance()
                right_distance = self.right_sensor.getDistance()
                front_distance = self.front_sensor.getDistance()
                ## Determine which way to turn
                print(left_distance)
                if(left_distance < right_distance):
                    if 10 < left_distance < 20:
                        self.servo.position = 350
                        print('Mid')
                    elif left_distance < 10:
                        self.servo.position = 425
                        print('Tourne à droite')
                        if 10 < left_distance < 20:
                            self.servo.position = 350"
                    elif left_distance > 20:
                        self.servo.position = 275
                        print('Tourne à gauche')
                        if 10 < left_distance < 20:
                            self.servo.position = 425
                    time.sleep(0.1)
                elif(right_distance < left_distance):
                    if 10 < right_distance < 20:
                        self.servo.position = 350
                        print('Mid')
                    elif right_distance < 10:
                        self.servo.position = 425
                        print('Tourne à droite')
                        if 10 < left_distance < 20:
                            self.servo.position = 350
                    elif right_distance > 20:
                        self.servo.position = 275
                        print('Tourne à gauche')
                        if 10 < left_distance < 20:
                            self.servo.position = 350
                    time.sleep(0.1)
                


        except KeyboardInterrupt:
            self.dc.stop()
            GPIO.cleanup()

sensorFollower = SensorFollower()
sensorFollower.follow_sensor()