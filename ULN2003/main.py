import Stepper
from machine import Pin
s1 = Stepper.create(Pin(0,Pin.OUT),Pin(1,Pin.OUT),Pin(2,Pin.OUT),Pin(3,Pin.OUT), delay=2)

# 接线
# ULN2003-树莓派Pico
# IN1-GPIO0
# IN2-GPIO1
# IN3-GPIO2
# IN4-GPIO3


s1.step(100)

s1.step(100,-1)

s1.angle(180)

s1.angle(360,-1)


# step设置509差不多angle设置360