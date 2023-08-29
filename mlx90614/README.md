


### 连线

|MLX90614|PICO|
|-|-|
|vcc|3v3|
|gnd|gnd|
|sda|5|
|scl|4|

PICO使用softI2C，与MLX90614 （GY-906）连接，波特率100000

### DEMO
```python
import mlx90614
from machine import Pin

from machine import SoftI2C as I2C
i2c = I2C(scl=Pin(4), sda=Pin(5),freq=100000)

sensor = mlx90614.MLX90614(i2c)

print(sensor.read_ambient_temp())#环境温度
print(sensor.read_object_temp()) #物体温度

```


原始库：
https://github.com/mcauser/micropython-mlx90614