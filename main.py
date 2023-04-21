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
            time.sleep(4.2)
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
            time.sleep(4.4)
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



class Circuit:
    def __init__(self, maxLapNumber: int):
        self.left_sensor = Ultrasonic(11, 9)
        self.front_sensor = Ultrasonic(6, 5)
        self.right_sensor = Ultrasonic(26, 19)
        self.servo = SensorAndMotor()
        self.dc = Dc()
        self.infra = Infra(20)
        self.maxLapNumber = maxLapNumber

    def run(self):
        self.dc.setup()
        self.dc.setSpeed(35)
        self.dc.forward()
        # servo positions
        self.center = 410
        self.lightLeft = 350
        self.lightRight = 490
        self.heavyLeft = 330
        self.heavyRight = 510

        # reset servo position
        self.servo.position = self.center

        threadInfra = threading.Thread(target=self.infra.run)
        threadInfra.start()

        try:
            while self.infra.lapNumber <= self.maxLapNumber:
                front_distance = self.front_sensor.getDistance()
                print(f"front distance: {front_distance}cm")

                # priority to the front sensor
                if front_distance < 20:
                    print(f"detected an obstacle at {front_distance}cm")
                    # slow down the car
                    self.dc.setSpeed(20)

                    # turn in the opposite direction of the nearest wall
                    if self.left_sensor.getDistance() < self.right_sensor.getDistance():
                        self.servo.position = self.heavyRight
                        print("Turning right")
                    else:
                        self.servo.position = self.heavyLeft
                        print("Turning left")
                else:
                    # return to normal speed
                    self.dc.setSpeed(35)
                    left_distance = self.left_sensor.getDistance()
                    right_distance = self.right_sensor.getDistance()
                    print(f"left distance: {left_distance}cm - right distance: {right_distance}cm")

                    if left_distance < right_distance:
                        if left_distance < 20:
                            self.servo.position = self.lightRight
                            print('Turning right\n')
                        else:
                            self.servo.position = self.center
                            print('Going straight\n')

                    elif left_distance > right_distance:
                        if right_distance < 20:
                            self.servo.position = self.lightLeft
                            print('Turning left\n')
                        else:
                            self.servo.position = self.center
                            print('Going straight\n')

                    # if the car is perfectly centered, do not turn
                    elif left_distance == right_distance:
                        self.servo.position = self.center

                time.sleep(0.01)
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
        self.servo.position = 410
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


print("1: circuit\n2: wall follower\n3: circle")
choice = input("> ")

if choice == "1":
    lapNumber = input("Nombre de tours (default=2): ")
    if lapNumber == "":
        lapNumber = 2
    circuit = Circuit(int(lapNumber))
    circuit.run()

elif choice == "2":
    wallFollower = FollowWall()
    wallFollower.followWall()

elif choice == "3":
    circle = Circle()
    circle.run()
