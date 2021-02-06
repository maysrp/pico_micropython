from hcsr04 import HCSR04
import time
sensor = HCSR04(trigger_pin=0, echo_pin=1)


# HCSR04 树莓派pico
#vcc--- 5v VBUS
#GND--- GND
#Trig--- 0
#echo--- 1

while True:
    m=sensor.distance_cm()
    print("Juli:",m,"cm")
    time.sleep(1)