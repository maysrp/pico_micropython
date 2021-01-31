from machine import I2C,Pin
from ssd1306 import SSD1306_I2C#I2C的oled选该方法
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000) 
oled = SSD1306_I2C(128, 64, i2c) #你的OLED分辨率，使用I2C
oled.fill(1) #清空屏幕
oled.show()
oled.fill(0)
oled.show()

oled.text("123",0,9,1)
oled.show()

oled.pixel(15,15,1)
oled.show()




# oled.pixel(x,y,z)
# x y处画点
# oled.line(x,y,x2,y2,c)直线
# oled.vline(x,y,l,c)
# oled.hline(x,y,l,c)