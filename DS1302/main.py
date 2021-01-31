from machine import Pin
import DS1302

ds = DS1302.DS1302(Pin(2),Pin(3),Pin(4))

# CLK GPIO2
# DAT GPIO3
# RST GPIO4
ds.DateTime()
# 返回 ：[2021, 1, 31, 7, 11, 10, 56]

ds.Year() #获取今天的年份
ds.Month() #获取今天的月份
ds.Day() #获取今天的日期
ds.Weekday() #获取当前周几
ds.Hour() #获取当前小时
ds.Minute() #获取当前分钟
ds.Second() #获取当前的秒

# 可以在以上函数中添加数字来设置时间
# 例如
ds.Year(2021) #设置今年为2021年
ds.Day(2)#设置今天为2号
