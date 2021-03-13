


import max7219
from machine import Pin,SPI
spi=SPI(0,baudrate=800000,sck=Pin(2), mosi=Pin(3), miso=Pin(0))
ss = Pin(1, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 4)
display.text('pico',0,0,1)
display.show()
display.pixel(20,7,1)
display.show()
display.line(0,0,31,4,1)
display.show()
display.hline(0,0,32,1)
display.show()
display.vline(2,3,4,1)
display.show()
display.fill(0)
display.show()
