import RPi.GPIO as GPIO
import Adafruit_PCA9685   
import time

pin1 = 11
pin2 = 12
en = 5
etat=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(pin1,GPIO.LOW)
GPIO.output(pin2,GPIO.LOW)
p=GPIO.PWM(en,1000)

p.start(30)
print("\n")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(etat==1):
         GPIO.output(pin1,GPIO.HIGH)
         GPIO.output(pin2,GPIO.LOW)
         print("Avancer")
        else:
         GPIO.output(pin1,GPIO.LOW)
         GPIO.output(pin2,GPIO.HIGH)
         print("Reculer")



    elif x=='s':
        print("La voiture s'arrête")
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.LOW)

    elif x=='f':
        print("La voiture avance")
        GPIO.output(pin1,GPIO.HIGH)
        GPIO.output(pin2,GPIO.LOW)
        etat=1

    elif x=='b':
        print("La voiture recule")
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.HIGH)
        temp1=0

    elif x=='l':
        print("Vitesse faible")
        p.ChangeDutyCycle(25)

    elif x=='m':
        print("Vitesse normale")
        p.ChangeDutyCycle(50)

    elif x=='h':
        print("Vitesse élevée")
        p.ChangeDutyCycle(75)
     
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  Veuillez entrer une des valeurs données  >>>")