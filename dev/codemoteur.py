import time
import Adafruit_PCA9685
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
pwm = Adafruit_PCA9685.PCA9685()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

def setMotor(mode):
    GPIO.output(27, mode)
    GPIO.output(15, not  mode)
    pwm.set_pwm(4,1024,3072)
    pwm.set_pwm_freq(1000)
    GPIO.output(17, mode)
    GPIO.output(18, not  mode)
    pwm.set_pwm(5,1024,3072)


i=0
try:
        while i<4:
                setMotor(GPIO.HIGH)
                time.sleep(5)
                setMotor(GPIO.LOW)
                time.sleep(5)
                i=i+1
finally:
        GPIO.output(27,GPIO.LOW)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
        GPIO.cleanup(18,GPIO.LOW)
