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


''' a tester
import time
from machine import I2C
from tcs34725 import TCS34725

i2c = I2C(2)

sensor = TCS34725(i2c)
sensor.integration_time = 200 # Valeur plus grande = plus d'information collectée

def corr_255(self):
    # Appliquer une correction gamma sur une valeur entre 0 - 255
    self.x /= 255
    self.x = pow(self.x, 2.5)
    self.self.x *= 255
    return int(self.x) if self.x < 255 else 255

def color(self):
    # corrAppliquer la correction gamma à un tuple de couleur rgb
    return corr_255(self.color[0]), corr_255(self.color[1]), corr_255(self.color[2])


while True:
    # Lecture de la couleur sur le capteur
    rgb = sensor.color_rgb_bytes    # color_rgb_bytes
    color_rgb = color( rgb )  # Appliquer correction Gamma
    print( "rgb : %s   color_rgb : %s" % (rgb, color_rgb) )
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