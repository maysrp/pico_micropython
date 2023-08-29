from machine import I2C,Pin
from bmp280 import *

bus = I2C(0,sda=Pin(0),scl=Pin(1), freq=400000)
bmp = BMP280(bus)

print(bmp.temperature)
print(bmp.pressure)
