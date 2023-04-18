import RPi.GPIO as GPIO          
import time

pin1 = 11
pin2 = 12
en = 5
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(pin1,GPIO.LOW)
GPIO.output(pin2,GPIO.LOW)
p=GPIO.PWM(en,1000)

p.start(25)
print("\n")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=raw_input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(pin1,GPIO.HIGH)
         GPIO.output(pin2,GPIO.LOW)
         print("Avancer")
         x='z'
        else:
         GPIO.output(pin1,GPIO.LOW)
         GPIO.output(pin2,GPIO.HIGH)
         print("Reculer")
         x='z'


    elif x=='s':
        print("Stop")
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.LOW)
        x='z'

    elif x=='f':
        print("Avancer")
        GPIO.output(pin1,GPIO.HIGH)
        GPIO.output(pin2,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("Reculer")
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  Wrong data, try again  >>>")