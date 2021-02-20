from machine import Pin
from DHT22 import DHT22
import utime

# DHT22 libray is available at
# https://github.com/danjperron/PicoDHT22

dht_sensor=DHT22(Pin(0,Pin.IN,Pin.PULL_UP),dht11=True)
T,H = dht_sensor.read()
# 正面
# VCC-DATA-none——GND