import board
import busio
import adafruit_ina219
import time
import RPi.GPIO as GPIO


# Initialisation de la communication I2C avec le capteur INA219
i2c = busio.I2C(board.SCL, board.SDA)
ina219 = adafruit_ina219.INA219(i2c)

def checkCurrent():
    current_mA = ina219.current
    print("Courant : %.2f mA" % current_mA)

def servoMoteur():
    # Initialise la communication avec le module PCA9685 via I2C
    i2c = busio.I2C(board.SCL, board.SDA)
    pca = adafruit_pca9685.PCA9685(i2c)

    # Configuration du servo-moteur
    servo_min = 150  # Pulse de 0.15 ms
    servo_max = 600  # Pulse de 0.60 ms
    servo_range = servo_max - servo_min

    # Configure la fréquence PWM (50 Hz pour les servo-moteurs)
    pca.frequency = 50



    # Fait tourner le servo-moteur dans un sens
    for pulse in range(servo_min, servo_max, 10):
        pca.channels[0].duty_cycle = int(pulse / servo_range * 65535)
        time.sleep(0.02)

    # Fait tourner le servo-moteur dans l'autre sens
    for pulse in range(servo_max, servo_min, -10):
        pca.channels[0].duty_cycle = int(pulse / servo_range * 65535)
        time.sleep(0.02)

while True:
    checkCurrent()
    servoMoteur()
    time.sleep(1)