import RPi.GPIO as GPIO
import unittest
import time
from sensors.Ultrasonic import Ultrasonic
from sensors.Infra import Infra



class TestInfra(unittest.TestCase):
    def test_infra(self):
        ir = Infra(20)
        result = ir.getInfo()
        self.assertEquals(1, result)


if __name__ == '__main__':
    unittest.main()