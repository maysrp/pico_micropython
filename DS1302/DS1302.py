'''
    DS1302 RTC drive

    Author: shaoziyang
    Date:   2018.3

    http://www.micropython.org.cn
'''
from machine import *

DS1302_REG_SECOND = (0x80)
DS1302_REG_MINUTE = (0x82)
DS1302_REG_HOUR   = (0x84)
DS1302_REG_DAY    = (0x86)
DS1302_REG_MONTH  = (0x88)
DS1302_REG_WEEKDAY= (0x8A)
DS1302_REG_YEAR   = (0x8C)
DS1302_REG_WP     = (0x8E)
DS1302_REG_CTRL   = (0x90)
DS1302_REG_RAM    = (0xC0)

class DS1302:
    def __init__(self, clk, dio, cs):
        self.clk = clk
        self.dio = dio
        self.cs  = cs
        self.clk.init(Pin.OUT)
        self.cs.init(Pin.OUT)
        
    def DecToHex(self, dat):
        return (dat//10) * 16 + (dat%10)

    def HexToDec(self, dat):
        return (dat//16) * 10 + (dat%16)

    def write_byte(self, dat):
        self.dio.init(Pin.OUT)
        for i in range(8):
            self.dio.value((dat >> i) & 1)
            self.clk.value(1)
            self.clk.value(0)

    def read_byte(self):
        d = 0
        self.dio.init(Pin.IN)
        for i in range(8):
            d = d | (self.dio.value()<<i)
            self.clk.value(1)
            self.clk.value(0)
        return d

    def getReg(self, reg):
        self.cs.value(1)
        self.write_byte(reg)
        t = self.read_byte()
        self.cs.value(0)
        return t

    def setReg(self, reg, dat):
        self.cs.value(1)
        self.write_byte(reg)
        self.write_byte(dat)
        self.cs.value(0)

    def wr(self, reg, dat):
        self.setReg(DS1302_REG_WP, 0)
        self.setReg(reg, dat)
        self.setReg(DS1302_REG_WP, 0x80)
                
    def start(self):
        t = self.getReg(DS1302_REG_SECOND + 1)
        self.wr(DS1302_REG_SECOND, t & 0x7f)

    def stop(self):
        t = self.getReg(DS1302_REG_SECOND + 1)
        self.wr(DS1302_REG_SECOND, t | 0x80)
        
    def Second(self, second = None):
        if second == None:
            return self.HexToDec(self.getReg(DS1302_REG_SECOND+1))%60
        else:
            self.wr(DS1302_REG_SECOND, self.DecToHex(second%60))

    def Minute(self, minute = None):
        if minute == None:
            return self.HexToDec(self.getReg(DS1302_REG_MINUTE+1))
        else:
            self.wr(DS1302_REG_MINUTE, self.DecToHex(minute%60))

    def Hour(self, hour = None):
        if hour == None:
            return self.HexToDec(self.getReg(DS1302_REG_HOUR+1))
        else:
            self.wr(DS1302_REG_HOUR, self.DecToHex(hour%24))

    def Weekday(self, weekday = None):
        if weekday == None:
            return self.HexToDec(self.getReg(DS1302_REG_WEEKDAY+1))
        else:
            self.wr(DS1302_REG_WEEKDAY, self.DecToHex(weekday%8))

    def Day(self, day = None):
        if day == None:
            return self.HexToDec(self.getReg(DS1302_REG_DAY+1))
        else:
            self.wr(DS1302_REG_DAY, self.DecToHex(day%32))

    def Month(self, month = None):
        if month == None:
            return self.HexToDec(self.getReg(DS1302_REG_MONTH+1))
        else:
            self.wr(DS1302_REG_MONTH, self.DecToHex(month%13))

    def Year(self, year = None):
        if year == None:
            return self.HexToDec(self.getReg(DS1302_REG_YEAR+1)) + 2000
        else:
            self.wr(DS1302_REG_YEAR, self.DecToHex(year%100))

    def DateTime(self, dat = None):
        if dat == None:
            return [self.Year(), self.Month(), self.Day(), self.Weekday(), self.Hour(), self.Minute(), self.Second()]
        else:
            self.Year(dat[0])
            self.Month(dat[1])
            self.Day(dat[2])
            self.Weekday(dat[3])
            self.Hour(dat[4])
            self.Minute(dat[5])
            self.Second(dat[6])

    def ram(self, reg, dat = None):
        if dat == None:
            return self.getReg(DS1302_REG_RAM + 1 + (reg%31)*2)
        else:
            self.wr(DS1302_REG_RAM + (reg%31)*2, dat)
