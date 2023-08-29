import time
from machine import Pin, I2C
import ina3221

i2c = I2C(0,scl=Pin(1), sda=Pin(0), freq=100000)
ina = ina3221.INA3221(i2c,0x40) #64

while True:
    print("CH1:",ina.getI(0),"mA")
    print("CH2:",ina.getI(1),"mA")
    print("CH3:",ina.getI(2),"mA")
    print("--------------------------")
    print("--------------------------")
    time.sleep(0.5)
               

