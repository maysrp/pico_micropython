请务必使用micropython1.18固件，1.19使用时候无法操作

IIC

|BMP180|PICO|
|-|-|
|SCL|1|
|SDA|0|
|CSB|VCC 3v3-OUT|
|SDO|GND|

```
from machine import I2C,Pin
from bmp280 import *

bus = I2C(0,sda=Pin(0),scl=Pin(1), freq=400000)
bmp = BMP280(bus)

print(bmp.temperature) #温度
print(bmp.pressure) #气压
```

库来自: https://github.com/Dafvid/micropython-bmp280
