#!/usr/bin/env python3
#coding: utf-8

import Adafruit_PCA9685

import adafruit_ina219
import board
import busio
import RPi.GPIO as GPIO
from time import sleep
from random import randint

class Servo:
    def __init__(self):
        self.__pwm = Adafruit_PCA9685.PCA9685()
        self.__pwm.set_pwm_freq(60)
        self.__position  = 375
        self.__SERVO_MIN = 150
        self.__SERVO_MAX = 500

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
        self.__pwm.set_pwm(0, 0, self.__position)

class Current:
    def __init__(self):
        # Initialisation de la communication I2C avec le capteur INA219
        i2c = busio.I2C(board.SCL, board.SDA)
        self.ina219 = adafruit_ina219.INA219(i2c)

    def checkCurrent(self) -> float:
        current_mA = self.ina219.current
        return current_mA

    def run(self):
        while True:
            current = self.checkCurrent()
            print("Courant : %.2f mA" % current)
            sleep(1)

class SensorAndMotor:
    def __init__(self):
        self.currentSensor = Current()
        self.servoMotor = Servo()
        self.infr = 20
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.infr, GPIO.IN)

    def checkCurrent(self):
        current_mA = self.currentSensor.checkCurrent()
        return current_mA

    def detectCriticalCurrent(self, threshold):
        current_mA = self.checkCurrent()
        # if current_mA > threshold:
        #     self.servoMotor.position = self.servoMotor.SERVO_MIN
        # else:
        #     self.servoMotor.position = self.servoMotor.SERVO_MAX
        while current_mA > threshold:
            if self.servoMotor.position > self.servoMotor.SERVO_MAX:
                self.servoMotor.position -= 10
            else:
                self.servoMotor.position += 10

    def run(self):
        while True:
            self.detectCriticalCurrent(500) # 500 mA is the threshold value
            self.servoMotor.position = randint(150, 500)
            sleep(1)

if __name__ == "__main__":
    sensorMotor = SensorAndMotor()
    sensorMotor.run()