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
