from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
DEFAULT_I2C_ADDR = 0x27
i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
#创建lcd对象用于显示
lcd.putstr("bilibili \n2021-1-30 20:35")
#显示文字 “bilibili \n2021-1-30 20:35” \n为换行符号
# lcd.clear()



#SDA GPIO0
#SCL GPIO1
#Vcc 5V （3V显示不清楚）
#GND GND

#若外置5V电源的话，请把外置电源的GND与树莓派的GND相连。
