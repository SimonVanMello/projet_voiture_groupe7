import RPi.GPIO as GPIO
from time import sleep

# Définition des pins
M1_In1 = 15
M1_In2 = 13
M1_En = 4

M2_In1 = 12
M2_In2 = 11
M2_En = 5

# Configuration des pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(M1_In1, GPIO.OUT)
GPIO.setup(M1_In2, GPIO.OUT)
GPIO.setup(M1_En, GPIO.OUT)

GPIO.setup(M2_In1, GPIO.OUT)
GPIO.setup(M2_In2, GPIO.OUT)
GPIO.setup(M2_En, GPIO.OUT)

# Configuration des objets PWM
M1_Vitesse = GPIO.PWM(M1_En, 1000)
M2_Vitesse = GPIO.PWM(M2_En, 1000)
M1_Vitesse.start(0)
M2_Vitesse.start(0)

# Fonction pour faire tourner les moteurs dans le sens 1
def sens1(moteurNum) :
    GPIO.output(Pins[moteurNum - 1][1], GPIO.HIGH)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
    M1_Vitesse.ChangeDutyCycle(50)
    M2_Vitesse.ChangeDutyCycle(50)
    print("Moteur", moteurNum, "tourne dans le sens 1.")

# Fonction pour faire tourner les moteurs dans le sens 2
def sens2(moteurNum) :
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.HIGH)
    M1_Vitesse.ChangeDutyCycle(50)
    M2_Vitesse.ChangeDutyCycle(50)
    print("Moteur", moteurNum, "tourne dans le sens 2.")

# Fonction pour arrêter un moteur
def arret(moteurNum) :
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
    M1_Vitesse.ChangeDutyCycle(0)
    M2_Vitesse.ChangeDutyCycle(0)
    print("Moteur", moteurNum, "arrêt.")

# Fonction pour arrêter complètement les moteurs
def arretComplet() :
    GPIO.output(M1_In1, GPIO.LOW)
    GPIO.output(M1_In2, GPIO.LOW)
    GPIO.output(M2_In1, GPIO.LOW)
    GPIO.output(M2_In2, GPIO.LOW)
    M1_Vitesse.ChangeDutyCycle(0)
    M2_Vitesse.ChangeDutyCycle(0)
    print("Moteurs arrêtés.")

# Arrêt complet des moteurs avant de commencer la boucle
arretComplet()

while True :
    # Exemple de motif de boucle
    sens1(1)
    sleep(3)
    sens1(2)
    sleep(3)
    arretComplet()
    sleep(5)
    sens2(1)
    sleep(2)
    arret(1)
    sleep(1)