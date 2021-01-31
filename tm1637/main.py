import tm1637
from machine import Pin
tm = tm1637.TM1637(clk=Pin(0), dio=Pin(1))

tm.numbers(12, 59)
tm.number(-123)
# tm.temperature(24) 不建议使用显示温度

# all LEDS on "88:88"
tm.write([127, 255, 127, 127])
# all LEDS off
tm.write([0, 0, 0, 0])
#一个列表每个代表一个led晶体管
# 数字8 由7个led管组成
# 8： 由8个led管组成