from machine import Pin
from MYUART import myUART
import time

c=Pin(2,Pin.OUT)
uart = myUART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)
c.value(0)
uart.write("AT C007")
time.sleep(1)
c.value(1)


