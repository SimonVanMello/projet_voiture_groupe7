#!/usr/bin/env python3
#coding: utf-8

import PCA9685 as p
import adafruit_ina219
import board
import busio
import RPi.GPIO as GPIO
import time
import threading
from random import randint

class Servo:
    def __init__(self):
        self.__pwm = p.PWM()
        self.__pwm.frequency = 50
        self.__position  = 225
        self.__SERVO_MIN = 250
        self.__SERVO_MAX = 525

    # getter function using property decorator
    @property
    def SERVO_MIN(self) -> int:
        return self.__SERVO_MIN

    @property
    def SERVO_MAX(self) -> int:
        return self.__SERVO_MAX

    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, newPosition: int):
        if newPosition in range(self.__SERVO_MIN, self.__SERVO_MAX):
            # whenever the position change with a valid value, we update
            # the actual position by calling self.__move()
            self.__position = newPosition
            self.__move()
            print(f"Position valide: {newPosition}")
        else:
            print(newPosition)
            print("Invalid value")

    def __move(self):
        self.__pwm.write(0, 0, self.__position)

class Current:
    def __init__(self):
        # Initialisation de la communication I2C avec le capteur INA219
        i2c = busio.I2C(board.SCL, board.SDA)
        self.ina219 = adafruit_ina219.INA219(i2c)

    def checkCurrent(self) -> float:
        current_mA = self.ina219.current
        return current_mA

    # test method
    def run(self):
        while True:
            current = self.checkCurrent()
            print("Courant : %.2f mA" % current)
            time.sleep(1)

class SensorAndMotor:
    def __init__(self):
        self.currentSensor = Current()
        self.servoMotor = Servo()
        self.infr = 20
        self.__position = self.servoMotor.position
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.infr, GPIO.IN)

    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, newPos: int):
        if newPos in range(self.servoMotor.SERVO_MIN, self.servoMotor.SERVO_MAX+1):
            self.__position = newPos
            self.servoMotor.position = self.__position
            # self.detectCriticalCurrent(500) # 500 mA is the threshold value

    def positionMid(self):
        self.servoMotor.position = 350

    def positionMin(self):
        self.servoMotor.position = 275

    def positionMax(self):
        self.servoMotor.position = 425

    def detectCriticalCurrent(self, threshold):
        current_mA = self.currentSensor.checkCurrent()
        

if __name__ == "__main__":
    sensorMotor = SensorAndMotor()
    # test the servo motor in 10 random positions
    for i in range(10):
        pos = randint(275, 450)
        print(f"Position: {pos}, current: {sensorMotor.currentSensor.checkCurrent()}mA")
        sensorMotor.position = pos
        time.sleep(2)
    # reset position
    sensorMotor.position = 350