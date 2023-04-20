import RPi.GPIO as GPIO
import time

# Configuration des broches GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(34, GPIO.IN) # Modifier le numéro de broche pour correspondre à votre câblage

# Boucle principale
try:
    while True:
        # Lecture des données du capteur
        valeur_capteur = GPIO.input(14)

        # Affichage de la valeur du capteur
        print("Valeur du capteur : {}".format(valeur_capteur))

        # Attente d'un court laps de temps avant de lire à nouveau
        time.sleep(0.1)

# Nettoyage des broches GPIO à la sortie
finally:
    GPIO.cleanup()

''' Code initial

import time
import board
import busio
import adafruit_tcs34725

# Configuration du capteur de couleur
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

while True:
    # Lit les valeurs de couleur
    r, g, b = sensor.color_rgb_bytes
    c = sensor.color_temperature

    # Affiche les valeurs dans la console
    print("Rouge : {}, Vert : {}, Bleu : {}".format(r, g, b))
    print("Température de couleur : {} K".format(c))
    time.sleep(1)

'''

''' EN COURS

import board
import adafruit_tcs34725
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)




print('Color: ({0}, {1}, {2})'.format(*sensor.color_rgb_bytes))
print('Temperature: {0}K'.format(sensor.color_temperature))
print('Lux: {0}'.format(sensor.lux))

'''