from machine import UART,Pin
import time
from neo6 import GPS

uart=UART(0,9600)


gps=GPS(uart)

while True:
    gps.getGPS()
    if(gps.FIX_STATUS == True):
        print("----------------------")
        print("维度: ","北纬" if "-" not in gps.latitude else "南纬",gps.latitude)
        print("经度: ","东经" if "-" not in gps.longitude else "西经",gps.longitude)
        print("卫星数: " ,gps.satellites)
        print("GPS时间: ",gps.GPStime)
        print("----------------------")
    gps.FIX_STATUS = False

    if(gps.TIMEOUT == True):
        print("无GPS信号")
        gps.TIMEOUT = False
