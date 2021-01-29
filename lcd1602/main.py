from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
DEFAULT_I2C_ADDR = 0x27
i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
#创建lcd对象用于显示
lcd.putstr("It Works!\nSecond Line")
#显示文字 “It Works! Second Line” \n为换行符号
lcd.clear()



#SDA GPIO0
#SCL GPIO1
