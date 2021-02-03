from machine import I2C,Pin
from ssd1306 import SSD1306_I2C#I2C的oled选该方法
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000) 
oled = SSD1306_I2C(128, 64, i2c) #你的OLED分辨率，使用I2C
from machine import ADC
import time

c=ADC(2)


oled.fill(1) #清空屏幕
oled.show()
oled.fill(0)
oled.show()



s=range(9000,11000)
x=range(19000,21000)
z=range(0,2000)
y=range(30000,32000)
q=range(45000,47000)

qr=False
p=[0,0]
 

m=[]
while True:
    oled.pixel(p[0],p[1],1)
    oled.show()
    time.sleep(0.1)
    oled.pixel(p[0],p[1],0)
    oled.show()

    u=c.read_u16()
    if u in q:
        qr=not qr
    elif u in s:
        p[1]=p[1]-1
    elif u in x:
        p[1]=p[1]+1
    elif u in z:
        p[0]=p[0]-1
    elif u in y:
        p[0]=p[0]+1
    else:
        pass
    if qr:
        if p not in m:
            nc=p*1
            m.append(nc)
    # print(m)
    for i in m:
        oled.pixel(i[0],i[1],1)
    oled.show()
    time.sleep(0.2)
