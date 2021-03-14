from machine import PWM,Pin

s=PWM(Pin(0))
s.freq(50)


s.duty_u16(1638)
#0度
s.duty_u16(4915)
#90度
s.duty_u16(8192)
#180度

#树莓派pico 一共可以使用16个PWM 本次使用GPIO0作为PWM
#MG996R 为5V 工作电压
# 红色 5V vbus
# 棕线 GND
# 黄线为 数据线
# ---------------
#20ms 一个周期 0.02==50hz
#0.5ms--0度
# 1.0ms--45度
# 1.5ms--90度
# 2.0ms--135度
# 2.5ms--180度
# 树莓派 为16位
# 即
# 0度 duty=65535*0.5/20
#     duty=1638

# 90度
# duty=65535*1.5/20
# duty=4915

# 180度
# duty=65535*2.5/20
# duty=8192                                                                                                                                                                                                                                                                                                                                                                                                                                           

