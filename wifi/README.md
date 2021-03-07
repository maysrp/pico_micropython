# wifiat_pico
PICO use WIFI  ESP8266 AT V1.1


## 介绍

该项目参考于[Raspberry-Pi-Pico-Wifi](https://github.com/tkraspi/Raspberry-Pi-Pico-Wifi)
ESP01 的版本号为1.1 版本较老，未测试其他版本的esp01，使用时请按照上面的连线测试

在HTTP请求不同域名的时候请先执行restart


## 连线
|PICO|ESP826601|
|-|-|
|GPIO0|RX|
|GPIO1|TX|
|3V3|3v3|
|3v3|EN|
|GND|GND|
 
 ## 测试代码
 
```
import utime
from machine import UART
from wifiat import at
uart=UART(0,115200)
AT=at(uart)

AT.info()

AT.restore()
#恢复出厂设置

AT.restart()


AT.netinfo()

AT.connect("wifi_name","wifi_password")

AT.netinfo()

AT.ping("baidu.com")

get=AT.http("http://httpbin.org/get")

post=AT.http("http://httpbin.org/post",method="POST",data='{"name":'tom',"AGE":'12'}',timeout=4)

print(get)

print(post)

AT.restart()
#使用不同域名时请先restart

utime.sleep(3)
get=AT.http("http://www.baidu.com")


#默认执行AT指令的方法
AT.sendCMD_waitResp("AT\r\n")
AT.sendCMD_waitRespLine("AT\r\n")
```

所有方法指令方法都有返回值请自行判断

