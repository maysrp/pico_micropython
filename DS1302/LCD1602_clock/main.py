import DS1302
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
import time
DEFAULT_I2C_ADDR = 0x27
i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

ds = DS1302.DS1302(Pin(2),Pin(3),Pin(4))

while True:
    d=ds.DateTime()
    date1=str(d[0])+"-"+str(d[1])+"-"+str(d[2])+" "+str(d[4])+":"+str(d[5])
    lcd.putstr(date1)
    time.sleep(1)
    lcd.clear()
    d=ds.DateTime()
    date2=str(d[0])+"-"+str(d[1])+"-"+str(d[2])+" "+str(d[4])+" "+str(d[5])
    lcd.putstr(date2)
    time.sleep(1)
    lcd.clear()
