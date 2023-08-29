 VL53L0X  激光测距传感器

 0-2m 范围
## demo
```python
from machine import Pin
from machine import SoftI2c as I2C
import vl53l0x

i2c = I2C(sda=Pin(4),scl=Pin(5), freq = 400000)
vl53 = vl53l0x.VL53L0X(i2c)

vl53.measurement_timing_budget = 20000 # microseconds

vl53.start_continuous()

while True:
    print("Range: {0}mm".format(vl53.range))
    time.sleep(1)
```

库：https://github.com/kapetan/MicroPython_VL53L0X
