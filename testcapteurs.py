import RPi.GPIO as GPIO
import time

# Configuration des broches GPIO
GPIO.setmode(GPIO.BOARD)
GPIO_TRIGGER = 29
GPIO_ECHO = 31
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # Envoie une impulsion sur la broche TRIGGER
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    # Calcul du temps de réponse
    pulse_start = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        pulse_start = time.time()

    pulse_end = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        pulse_end = time.time()

    # Calcule la distance en cm
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

try:
    while True:
        dist = distance()
        print("Distance : {} cm".format(dist))
        time.sleep(1)
except KeyboardInterrupt:
    print("Programme arrêté par l'utilisateur")
finally:
    GPIO.cleanup()