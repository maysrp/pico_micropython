from machine import I2C,Pin
from ssd1306 import SSD1306_I2C#I2C的oled选该方法
import framebuf

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000) 
oled = SSD1306_I2C(128, 64, i2c) #你的OLED分辨率，使用I2C
oled.fill(1) #清空屏幕
oled.show()

with open("a.pbm",'rb') as f :
	f.readline()
	f.readline()
	data = bytearray(f.read())
fbuf = framebuf.FrameBuffer(data,86,64,framebuf.MONO_HLSB)
# fbuf = framebuf.FrameBuffer(data,128,64,framebuf.MONO_HLSB)
oled.fill(0)
oled.blit(fbuf,0,0)
oled.show()