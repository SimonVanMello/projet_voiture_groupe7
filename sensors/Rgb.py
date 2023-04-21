#!/usr/bin/env python3
#coding: utf-8

import board
import adafruit_tcs34725

class Rgb:
    def __init__(self):
        self.i2c = board.I2C()
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c)

    def getColors(self):
        colors = ('{0} {1} {2}'.format(*self.sensor.color_rgb_bytes)).split(' ')
        self.red = colors[0]
        self.green = colors[1]

    def getGreen(self):
        self.getColors()
        return int(self.green)

    def getRed(self):
        self.getColors()
        return int(self.red)

if __name__  == "__main__":
    rgb = Rgb()
    print(f"Red: {rgb.getRed()} - green: {rgb.getGreen()}")