from machine import ADC
import time
# 34号
c=ADC(2)
c.read_u16()

s=range(9000,11000)
x=range(19000,21000)
z=range(0,2000)
y=range(30000,32000)
q=range(45000,47000)

while True:
    cc=c.read_u16()
    if cc in s:
        print("s")
    elif cc in x:
        print("x")
    elif cc in z:
        print("z")
    elif cc in y:
        print("y")
    elif cc in q:
        print("q")
    else:
        print("0")
    time.sleep(0.5)
# 不按60000以上
#     上(9000-11000)
# 左(0-2000)      右(30000-32000)          外(45000-47000)
#     下(19000-21000)
