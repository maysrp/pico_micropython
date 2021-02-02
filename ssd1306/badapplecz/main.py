from machine import I2C,Pin
from ssd1306 import SSD1306_I2C#I2C的oled选该方法
import framebuf
import ujson as json
import time
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=2000000) 
oled = SSD1306_I2C(128, 64, i2c) #你的OLED分辨率，使用I2C
oled.fill(1) #清空屏幕
oled.show()

def image(img_list):  
    e=time.ticks_ms() 
    oled.fill(0)     
    for i in img_list:
        oled.hline(2*i[0],2*i[1],2*i[2],1)
        oled.hline(2*i[0],2*i[1]+1,2*i[2],1)
    oled.show()
    d=time.ticks_ms()
    q=100-(d-e)
    if q>0:
        time.sleep(q/1000)
with open('bad.data','r') as f:
    c=0
    for i in f:
        c=c+1
        try:
            z=json.loads(i)
            image(z)
        except Exception as e:
            pass