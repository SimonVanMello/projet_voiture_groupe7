#!/usr/bin/env python3
#coding: utf-8

import RPi.GPIO as GPIO
import PCA9685 as p
import time

class Dc:
    def __init__(self):
        # ===========================================================================
        # Raspberry Pi pin11, 12, 13 and 15 to realize the clockwise/counterclockwise
        # rotation and forward and backward movements
        # ===========================================================================
        self.Motor0_A = 11  # pin11
        self.Motor0_B = 12  # pin12
        self.Motor1_A = 13  # pin13
        self.Motor1_B = 15  # pin15
        # ===========================================================================
        # Set channel 4 and 5 of the DC motor driver IC to generate PWM, thus 
        # controlling the speed of the car
        # ===========================================================================
        self.EN_M0    = 4  # servo driver IC CH4
        self.EN_M1    = 5  # servo driver IC CH5
        self.pins = [self.Motor0_A, self.Motor0_B, self.Motor1_A, self.Motor1_B]

    def setSpeed(self, speed):
        speed *= 40
        print ('speed is: ', speed)
        self.pwm.write(self.EN_M0, 0, speed)
        self.pwm.write(self.EN_M1, 0, speed)

    def setup(self, busnum=None):
        global forward0, forward1, backward1, backward0
        global pwm
        if busnum == None:
            self.pwm = p.PWM()                  # Initialize the servo controller.
        else:
            self.pwm = p.PWM(bus_number=busnum) # Initialize the servo controller.

        self.pwm.frequency = 60
        self.forward0 = 'True'
        self.forward1 = 'True'
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)        # Number GPIOs by its physical location
        try:
            for line in open("config"):
                if line[0:8] == "forward0":
                    self.forward0 = line[11:-1]
                if line[0:8] == "forward1":
                    self.forward1 = line[11:-1]
        except:
            pass
        if self.forward0 == 'True':
            self.backward0 = 'False'
        elif self.forward0 == 'False':
            self.backward0 = 'True'
        if self.forward1 == 'True':
            self.backward1 = 'False'
        elif self.forward1 == 'False':
            self.backward1 = 'True'
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
        
    def motor0(self, x):
        if x == 'True':
            GPIO.output(self.Motor0_A, GPIO.LOW)
            GPIO.output(self.Motor0_B, GPIO.HIGH)
        elif x == 'False':
            GPIO.output(self.Motor0_A, GPIO.HIGH)
            GPIO.output(self.Motor0_B, GPIO.LOW)
        else:
            print('Config Error')

    def motor1(self, x):
        if x == 'True':
            GPIO.output(self.Motor1_A, GPIO.LOW)
            GPIO.output(self.Motor1_B, GPIO.HIGH)
        elif x == 'False':
            GPIO.output(self.Motor1_A, GPIO.HIGH)
            GPIO.output(self.Motor1_B, GPIO.LOW)

    def forward(self):
        self.motor0(self.forward0)
        self.motor1(self.forward1)

    def backward(self):
        self.motor0(self.backward0)
        self.motor1(self.backward1)

    def forwardWithSpeed(self, spd = 50):
        self.setSpeed(spd)
        self.motor0(self.forward0)
        self.motor1(self.forward1)

    def backwardWithSpeed(self, spd = 50):
        self.setSpeed(spd)
        self.motor0(self.backward0)
        self.motor1(self.backward1)

    def stop(self):
        for pin in self.pins:
            GPIO.output(pin, GPIO.LOW)

    def ctrl(self, status, direction=1):
        if status == 1:   # Run
            if direction == 1:     # Forward
                self.forward()
            elif direction == -1:  # Backward
                self.backward()
            else:
                print('Argument error! direction must be 1 or -1.')
        elif status == 0: # Stop
            self.stop()
        else:
            print('Argument error! status must be 0 or 1.')

    def test():
        while True:
            self.setup()
            self.ctrl(1)
            time.sleep(3)
            self.setSpeed(10)
            time.sleep(3)
            self.setSpeed(100)
            time.sleep(3)
            self.ctrl(0)

try:
        dc = Dc()
        dc.setup()
        dc.setSpeed(10)
        print("1: forward\n2: backward")
        choice = input("> ")
        if choice not in ["1", "2"]:
            print("Invalid choice")
            exit
        elif choice == "1":
            dc.forward()
        else:
            dc.backward()
        while True:    
            nn = input()
            if nn == "stop":
                dc.stop()
                break
                exit
            else:
                dc.setSpeed(int(nn))
finally:                # this block will run no matter how the try block exits  
    exit                # clean up after yourself