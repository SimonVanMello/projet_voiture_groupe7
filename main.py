#!/usr/bin/env python3
#coding: utf-8

from motors.Dc import Dc
from motors.Servo import SensorAndMotor
from sensors.Ultrasonic import Ultrasonic
from sensors.Infra import Infra
import time
import RPi.GPIO as GPIO
import threading

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
        self.left_sensor = Ultrasonic(11, 9)
        self.front_sensor = Ultrasonic(6, 5)
        self.right_sensor = Ultrasonic(26, 19)
        self.servo = SensorAndMotor()
        self.dc = Dc()
        self.infra = Infra(20)

    def getPositionFromDistance(self, prox_wall: str, distance: float) -> int:
        print(f"proxWall: {prox_wall} - distance: {distance}")
        if prox_wall == "right":
            # turn left
            # if distance < 10:
            return 340
            # elif distance < 20:
            #     return 350
            # elif distance <= 30:
            #     return 360
        elif prox_wall == "left":
            # turn right
            # if distance < 10:
            return 500
            # elif distance < 20:
            #     return 500
            # elif distance <= 30:
            #     return 490

    def follow_sensor(self):
        self.dc.setup()
        self.dc.setSpeed(30)
        self.dc.forward()
        self.prox_wall = ''
        threadInfra = threading.Thread(target=self.infra.run)
        threadInfra.start()
        try:
            while self.infra.lapNumber <= 2:
                left_distance = self.left_sensor.getDistance()
                right_distance = self.right_sensor.getDistance()
                front_distance = self.front_sensor.getDistance()
                print(f"front distance: {front_distance}")

                if left_distance < right_distance:
                    self.prox_wall = "left"
                else:
                    self.prox_wall = "right"

                # Determine which way to turn
                print(f"left_distance: {left_distance} - right_distance: {right_distance}")
                if front_distance < 20:
                    print(f"detected an obstacle at {front_distance}cm")
                    self.servo.position = self.getPositionFromDistance(self.prox_wall, front_distance)
                    time.sleep(1)
                    self.servo.position = 410

                elif left_distance < right_distance:
                    if left_distance < 20:
                        self.servo.position = 500
                        print('Tourne à droite')
                    else:
                        self.servo.position = 410
                        print('Mid')

                elif left_distance > right_distance:
                    if right_distance < 20:
                        self.servo.position = 340
                        print('Tourne à gauche')
                    else:
                        self.servo.position = 410
                        print('Mid')
                time.sleep(0.1)
            self.dc.stop()
            GPIO.cleanup()
        except KeyboardInterrupt:
            self.dc.stop()
            GPIO.cleanup()

class FollowWall:
    def __init__(self):
        self.left_sensor = Ultrasonic(11, 9)
        self.right_sensor = Ultrasonic(26, 19)
        self.servo = SensorAndMotor()
        self.dc = Dc()

    def followWall(self):
        self.dc.setup()
        self.dc.setSpeed(30)
        self.dc.forward()
        
        try:
            while True:
                left_distance = self.left_sensor.getDistance()
                right_distance = self.right_sensor.getDistance()

                
                if left_distance < right_distance:
                    if 20 < left_distance < 40:
                        self.servo.position = 410
                        print('Mid')
                    elif left_distance < 20:
                        self.servo.position = 480
                        print('Tourne à droite')
                    elif left_distance > 40:
                        self.servo.position = 360
                        print('Tourne à gauche')

                elif right_distance <= left_distance:
                    if 20 < right_distance < 40:
                        self.servo.position = 410
                        print('Mid')
                    elif right_distance < 20:
                        self.servo.position = 360
                        print('Tourne à droite')
                    elif right_distance > 40:
                        self.servo.position = 480
                        print('Tourne à gauche')
                time.sleep(0.01)
            self.dc.stop()
            GPIO.cleanup()
        except KeyboardInterrupt:
            self.dc.stop()
            GPIO.cleanup()


print("1: main\n2: wall follower\n3: circle")
choice = input("> ")

if choice == "1":
    sensorFollower = SensorFollower()
    sensorFollower.follow_sensor()
elif choice == "2":
    wallFollower = FollowWall()
    wallFollower.followWall()
elif choice == "3":
    circle = Circle()
    circle.run()
