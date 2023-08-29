## 使用

### 接线方式 

|HW-040|Pico|
|-|-|
|GND|GND|
|3v3|3v3|
|CLK|2|
|DT|1|
|SW|0|

### 测试代码

```python
import time
from machine import Pin
from rotary_irq_rp2 import RotaryIRQ
#根据不同的设备导入不同的rotrotary_irq_xxx,请自行查看。
r = RotaryIRQ(pin_num_clk=2, 
              pin_num_dt=1, 
              min_val=0, 
              max_val=10, 
              reverse=False, 
              range_mode=RotaryIRQ.RANGE_WRAP)

button=Pin(0,Pin.IN,Pin.PULL_UP)              
val_old = r.value()
while True:
    val_new = r.value()
    
    if val_old != val_new:
        val_old = val_new
        print('result =', val_new)
    if button.value() ==0:
        print("按钮被按下")
        
    time.sleep_ms(50)
```



库来自于 https://github.com/miketeachman/micropython-rotary