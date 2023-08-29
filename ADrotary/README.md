
|Rotation sensor|pico|
|-|-|
|GND|GND|
|vcc|3v3|
|OUT|26|

```python
from machine import ADC
import time
c=ADC(0)# GPIO26 ADC为0
while True:
    print(c.read_u16())
    time.sleep(0.1)
```
ADC值为 65535-0 间

只能转360度

