from time import sleep
import RPi.GPIO as GPIO

# Modifiez pour mettre les pins sur lesquels sont branchés les entrées de la L293D
MOTOR1_EN = 4
MOTOR1_A = 11
MOTOR1_B = 12

MOTOR2_EN = 5
MOTOR2_A = 15
MOTOR2_B = 13

try:

    # Configure les pins
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(MOTOR1_EN, GPIO.OUT)
    GPIO.setup(MOTOR1_A, GPIO.OUT)
    GPIO.setup(MOTOR1_B, GPIO.OUT)

    GPIO.setup(MOTOR2_EN, GPIO.OUT)
    GPIO.setup(MOTOR2_A, GPIO.OUT)
    GPIO.setup(MOTOR2_B, GPIO.OUT)

    motor1GPIO = GPIO.PWM(MOTOR1_EN, 100)
    motor2GPIO = GPIO.PWM(MOTOR2_EN, 100)

    # AVANCE

    # Fais avancer le robot lentement (50%) en ligne droite
    motor1GPIO.start(50)
    GPIO.output(MOTOR1_A, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.LOW)

    motor2GPIO.start(50)
    GPIO.output(MOTOR2_A, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.LOW)

    # Continu d'avancer pendant une seconde et demi
    sleep(1.5)

    # RECULE EN TOURNANT

    # Fais reculer le robot en dessinant une courbe
    motor1GPIO.start(100)
    GPIO.output(MOTOR1_A, GPIO.LOW)
    GPIO.output(MOTOR1_B, GPIO.HIGH)

    motor2GPIO.start(60)
    GPIO.output(MOTOR2_A, GPIO.LOW)
    GPIO.output(MOTOR2_B, GPIO.HIGH)

    # Continu de reculer pendant 2 secondes
    sleep(2)

    # Arrêt des moteurs en arrêtant les cycles de travail
    motor1GPIO.stop()
    motor2GPIO.stop()


except KeyboardInterrupt:
    pass
except:
    GPIO.cleanup()
    raise

GPIO.cleanup()