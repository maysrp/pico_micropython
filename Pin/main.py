from machine import Pin

l=Pin(0,Pin.OUT)
l.high()
l.low()

l.value()
l.value(1)
l.value(0)

#按钮

#GPIO 1 和 按钮 和 GND相连


b=Pin(1,Pin.OUT)
b.value(1)

b.value()

#按钮按下

b.value()


