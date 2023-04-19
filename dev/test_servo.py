#!/usr/bin/env python
import PCA9685 as servo
import time                  # Import necessary modules

MinPulse = 250
MaxPulse = 450

def setup():
    global pwm
    pwm = servo.PWM()
    pwm.frequency = 50

def servo_test():
    inp = ""
    while inp != "stop":
        try:
            if int(inp) in range(MinPulse, MaxPulse+1):
                pwm.write(0, 0, int(inp))
            else:
                print(f"Not in range [{MinPulse}, {MaxPulse}]")
            inp = input("> ")
        except:
            print("Incorrect value")
    pwm.write(0, 0, 350)

if __name__ == '__main__':
    setup()
    servo_test()