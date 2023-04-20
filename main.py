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
        self.prox_wall=''
        try:
            while True:
                left_distance = self.left_sensor.getDistance()
                right_distance = self.right_sensor.getDistance()
                front_distance = self.front_sensor.getDistance()
                print(f"front distance: {front_distance}")

                ## Determine which way to turn
                print(left_distance)
                if front_distance < 30:
                    print(f"detected an obstacle at {front_distance}cm")
                    if self.prox_wall == 'left':
                        print("turning right")
                        self.servo.position = 500 #turn right
                    elif self.prox_wall == 'right':
                        print("turning left")
                        self.servo.position =350  #turn left

                elif(left_distance < right_distance):
                    self.prox_wall='left'
                    if 20 < left_distance < 40:
                        self.servo.position = 400
                        print('Mid')
                    elif left_distance < 20:

                        self.servo.position = 500
                        print('Tourne à droite')
                    elif left_distance > 40:
                        self.servo.position = 350
                        print('Tourne à gauche')

                elif(right_distance < left_distance):
                    self.prox_wall='righ'
                    if 20 < right_distance < 40:
                        self.servo.position = 400
                        print('Mid')
                    elif right_distance < 20:
                        self.servo.position = 500
                        print('Tourne à droite')
                    elif right_distance > 40:
                        self.servo.position = 350
                        print('Tourne à gauche')
                        time.sleep(0.1)


        except KeyboardInterrupt:
            self.dc.stop()
            GPIO.cleanup()

sensorFollower = SensorFollower()
sensorFollower.follow_sensor()