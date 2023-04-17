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
