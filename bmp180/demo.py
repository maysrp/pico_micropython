from bmp180 import BMP180
from machine import Pin
from machine import SoftI2C as I2C
from time import sleep

i2c = I2C(scl=Pin(1), sda=Pin(0),freq=100000)
bmp = BMP180(i2c)


print(bmp.temperature)
print(bmp.pressure)