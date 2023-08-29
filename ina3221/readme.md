注意:必须使用3.3V
建议将A0与GND一起焊接（用焊锡相连）这样IIC地址就为）0x40

相关地址

|A0连接|address|
|-|-|
|GND|0x40|
|VS|0x41|
|SDA|0x42|
|SCL|0x43|

接线(目前使用IIC 0 可以根据PICO的引脚自行切换对应的IIC)

CH1 CH2 CH3 接线请不要接错 VIN+ VIN-

|INA3221|PICO|
|-|-|
|SDA|GP0|
|SCL|GP1|
|vcc(vs)|3v3|
|gnd|gnd|


上传文件ina3221.py,接线后使用测试文件ex3221.py。

每次测量电流为12ms左右，默认取20次测量平均数。

相关信息参考:
https://github.com/roarnyg/INA3221-Micropython
https://github.com/PilotXing/ina3221
https://e2e.ti.com/support/amplifiers-group/amplifiers/f/amplifiers-forum/470422/ina3221---i2c-comms-issue#:~:text=The%20addressing%20is%20done%20as%20shown%20below%2C%20IC8,has%20the%20address%200x43%20%28according%20to%20the%20datasheet%29.


4电机测量

A-INA3221与B-INA3221 之间的地址必须不一样，（即必须修改AO的地址）
|A-INA3221|B-INA3221|PICO|
|-|-|-|
|SDA|SDA|GP0|
|SDA|SDA|GP1|
|vcc(vs)|vcc(vs)|3v3|
|gnd|gnd|gnd|
