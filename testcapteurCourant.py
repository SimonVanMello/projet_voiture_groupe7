import board
import busio
import adafruit_ina219
import time
import RPi.GPIO as GPIO


# Initialisation de la communication I2C avec le capteur INA219
i2c = busio.I2C(11, 12)
ina219 = adafruit_ina219.INA219(i2c)
def checkCurrent():
    current_mA = ina219.current

    print("Courant : %.2f mA" % current_mA)
def servoMoteur():


    # Configuration des broches GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)

    # Initialisation de la broche PWM pour le servo-moteur
    servo = GPIO.PWM(18, 50)  # 50Hz est la fréquence standard pour les servo-moteurs

    # Démarrage du signal PWM
    servo.start(0)

    try:

        # Déplace le servo-moteur à 0 degré (position la plus à gauche)
        servo.ChangeDutyCycle(2)
        time.sleep(1)

        # Déplace le servo-moteur à 90 degrés (position centrale)
        servo.ChangeDutyCycle(7)
        time.sleep(1)

        # Déplace le servo-moteur à 180 degrés (position la plus à droite)
        servo.ChangeDutyCycle(12)
        time.sleep(1)

    except KeyboardInterrupt:
        # Arrêt du signal PWM et nettoyage des broches GPIO
        servo.stop()
        GPIO.cleanup()
while true:
    servoMoteur()
    checkCurrent()


    time.sleep(1)