from machine import I2C,Pin
import time
from servo import Servos
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=10000)
s=Servos(i2c,address=0x40)
s.position(0,0)
s.position(1,0)
s.position(0,90)
s.position(1,90)

#pico-PCA9685

#3v3 OUT--VCC
#GND--GND
#GPIO0--SDA
#GPIO1--SCL


#PCA 9685 接线
#0-15为外接舵机
#外接5V电源
#黄色 数据
#红色 5V