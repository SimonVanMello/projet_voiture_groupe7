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
    import time
    from adafruit_servokit import ServoKit

    kit = ServoKit(channels=16)

    # Initialise le servo-moteur connecté au canal 0 avec une fréquence de 50 Hz
    kit.servo[0].set_pulse_width_range(500, 2500)
    kit.servo[0].actuation_range = 180
    kit.servo[0].frequency = 50

    # Fait tourner le servo-moteur de 0 à 180 degrés en incrémentant de 10 degrés toutes les 0.5 secondes
    for angle in range(0, 181, 10):
        kit.servo[0].angle = angle
        time.sleep(0.5)

    # Fait tourner le servo-moteur de 180 à 0 degrés en incrémentant de 10 degrés toutes les 0.5 secondes
    for angle in range(180, -1, -10):
        kit.servo[0].angle = angle
        time.sleep(0.5)

    # Arrête le servo-moteur
    kit.servo[0].angle = None
while true:
    servoMoteur()
    checkCurrent()


    time.sleep(1)