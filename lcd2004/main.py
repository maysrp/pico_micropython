from machine import I2C, Pin
from lcd2004 import LCD2004
i2c = I2C(0, freq=400000) 
lcd = LCD2004(i2c, addr=39)