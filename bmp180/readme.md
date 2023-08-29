BMP180

|BMP180|PICO|
|-|-|
|VCC|vcc 3v3-OUT|
|GND|GND|
|SDA|0|
|SCL|1|


注意树莓派pico (1.18) 必须使用 SoftI2C 才能使用。
freq=100000

```
from bmp180 import BMP180
from machine import Pin
from machine import SoftI2C as I2C
from time import sleep

i2c = I2C(scl=Pin(1), sda=Pin(0),freq=100000)
bmp = BMP180(i2c)


print(bmp.temperature) #温度
print(bmp.pressure) #气压

```

库来自于：https://github.com/micropython-IMU/micropython-bmp180
