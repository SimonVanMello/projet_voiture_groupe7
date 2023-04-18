import PCA9685 as p
from time import sleep   # Import necessary modules

# Set the motor pins to the appropriate channel on the PCA9685
Motor0 = 0  # Motor 1 is connected to channel 0 on the PCA9685
Motor1 = 1  # Motor 2 is connected to channel 1 on the PCA9685

# Set the PWM channels for controlling the motor speed
EN_M0 = 4  # PWM channel for controlling the speed of Motor 1
EN_M1 = 5  # PWM channel for controlling the speed of Motor 2

# Initialize the PWM controller
pwm = p.PWM()

# Set the PWM frequency
pwm.frequency = 60

# Set the initial speed of the motors
speed = 50

# Define the motor control functions
def motor0(x):
    # Motor 1
    if x == 'True':
        pwm.write(Motor0, 4095, 0)
    elif x == 'False':
        pwm.write(Motor0, 0, 4095)
    else:
        print ('Config Error')

def motor1(x):
    # Motor 2
    if x == 'True':
        pwm.write(Motor1, 4095, 0)
    elif x == 'False':
        pwm.write(Motor1, 0, 4095)
    else:
        print ('Config Error')

def setSpeed(spd):
    global speed
    speed = spd
    pwm.write(EN_M0, 0, speed*16)
    pwm.write(EN_M1, 0, speed*16)

def setup():
    # Initialize the PCA9685
    pwm.setup()

def forward():
    motor0('True')
    motor1('True')

def backward():
    motor0('False')
    motor1('False')

def forwardWithSpeed(spd = 50):
    setSpeed(spd)
    motor0('True')
    motor1('True')

def backwardWithSpeed(spd = 50):
    setSpeed(spd)
    motor0('False')
    motor1('False')

def stop():
    motor0(None)
    motor1(None)

def test():
    setup()
    forwardWithSpeed(50)
    sleep(3)
    setSpeed(10)
    forwardWithSpeed(10)
    backwardWithSpeed(10)
    sleep(3)
    setSpeed(100)
    forwardWithSpeed(100)
    backwardWithSpeed(100)
    sleep(3)
    stop()

if __name__ == '__main__':
    test()