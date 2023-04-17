import board
import busio
import adafruit_ina219

# Initialisation de la communication I2C avec le capteur INA219
i2c = busio.I2C(11, 12)
ina219 = adafruit_ina219.INA219(i2c)

# Lecture de la valeur de courant
while true:
    current_mA = ina219.current

    print("Courant : %.2f mA" % current_mA)
    sleep(1)