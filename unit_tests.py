#!/usr/bin/env python3
#coding: utf-8

from motors.Dc import Dc
from motors.Servo import SensorAndMotor
import RPi.GPIO as GPIO
from sensors.Infra import Infra
from sensors.Ultrasonic import Ultrasonic
from sensors.Rgb import Rgb
import time
import unittest

class TestUltrasonic(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # this is the expected value in cm
        self.distance = 14
        self.borninf = self.distance - (self.distance/11.25)
        self.bornsup = self.distance + (self.distance/11.25)
        super().setUpClass()

    def test_left_mesure(self):
        leftSensor = Ultrasonic(11,9)
        distance = leftSensor.getDistance()
        print(f"Distance mesured: {distance}")
        self.assertTrue(self.borninf <= distance <= self.bornsup, f"left distance: {distance}")

    def test_front_mesure(self):
        frontSensor = Ultrasonic(6,5)
        distance = frontSensor.getDistance()
        print(f"Distance mesured: {distance}")
        self.assertTrue(self.borninf <= distance <= self.bornsup, f"front distance: {distance}")

    def test_right_mesure(self):
        rightSensor = Ultrasonic(26, 19)
        distance = rightSensor.getDistance()
        print(f"Distance mesured: {distance}")
        self.assertTrue(self.borninf <= distance <= self.bornsup, f"right distance: {distance}")
        

class TestInfra(unittest.TestCase):
    def test_infra(self):
        ir = Infra(20)
        result = ir.getInfo()
        self.assertEquals(1, result)


class TestSensorAndMotor(unittest.TestCase):
    def setUp(self):
        self.sensorMotor = SensorAndMotor()

    def test_position(self):
        # test that setting position to a valid value works
        self.sensorMotor.position = 275
        self.assertEqual(self.sensorMotor.position, 275)

    def test_wrong_position(self):
        self.sensorMotor.position = 100
        self.assertEqual(self.sensorMotor.position, 275)

    def test_positionMid(self):
        # test that positionMid() sets the position to 350
        self.sensorMotor.positionMid()
        self.assertEqual(self.sensorMotor.position, 350)

    def test_positionMin(self):
        # test that positionMin() sets the position to 275
        self.sensorMotor.positionMin()
        self.assertEqual(self.sensorMotor.position, 275)

    def test_positionMax(self):
        # test that positionMax() sets the position to 425
        self.sensorMotor.positionMax()
        self.assertEqual(self.sensorMotor.position, 425)


class Testmoteurs(unittest.TestCase):
    def setUp(self):
        self.dcmotor = Dc()
        self.dcmotor.setup()

    def testSetSpeedForward(self):
        self.dcmotor.forward()
        self.dcmotor.setSpeed(30)
        self.assertEqual(self.dcmotor.speed, 30*40)
        time.sleep(2)
        self.dcmotor.stop()
    
    def testSetSpeedBackward(self):
        self.dcmotor.backward()
        self.dcmotor.setSpeed(30)
        self.assertEqual(self.dcmotor.speed, 30*40)
        time.sleep(2)
        self.dcmotor.stop()


class TestRgb(unittest.TestCase):
    def setUp(self):
        self.rgb = Rgb()
    
    def testGreen(self):
        self.assertTrue(self.rgb.getGreen() > self.rgb.getRed(), "plus de vert que de rouge ?")
    
    def testRed(self):
        self.assertTrue(self.rgb.getGreen() < self.rgb.getRed(), "+ de rouge que de vert ?")


if __name__ == '__main__':
    print("0: exit\n1: ultrasonic\n2: infrared\n3: servo\n4: dc motor\n5: rgb")
    inp = input("> ")
    if inp == "1":
        unittest.main(TestUltrasonic())
    elif inp == "2":
        unittest.main(TestInfra())
    elif inp == "3":
        unittest.main(TestSensorAndMotor())
    elif inp == "4":
        unittest.main(Testmoteurs())
    elif inp == "5":
        unittest.main(TestRgb())