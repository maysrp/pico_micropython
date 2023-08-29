from machine import I2C, Pin, Timer
from micropython import const
import time

_REG_CONFIG                      = const(0x00)

_RESET                           = const(0x8000)
_ENABLE_CH                       = (None,const(0x4000),const(0x2000),const(0x1000)) # default set

_AVERAGING_MASK                  = const(0x0E00)
_AVERAGING_NONE                  = const(0x0000)     # 1 sample, default
_AVERAGING_4_SAMPLES             = const(0x0200)
_AVERAGING_16_SAMPLES            = const(0x0400)
_AVERAGING_64_SAMPLES            = const(0x0600)
_AVERAGING_128_SAMPLES           = const(0x0800)
_AVERAGING_256_SAMPLES           = const(0x0A00)
_AVERAGING_512_SAMPLES           = const(0x0C00)
_AVERAGING_1024_SAMPLES          = const(0x0E00)

_VBUS_CONV_TIME_MASK             = const(0x01C0)
_VBUS_CONV_TIME_140US            = const(0x0000)
_VBUS_CONV_TIME_204US            = const(0x0040)
_VBUS_CONV_TIME_332US            = const(0x0080)
_VBUS_CONV_TIME_588US            = const(0x00C0)
_VBUS_CONV_TIME_1MS              = const(0x0100)     # 1.1ms, default
_VBUS_CONV_TIME_2MS              = const(0x0140)     # 2.116ms
_VBUS_CONV_TIME_4MS              = const(0x0180)     # 4.156ms
_VBUS_CONV_TIME_8MS              = const(0x01C0)     # 8.244ms

_SHUNT_CONV_TIME_MASK            = const(0x0038)
_SHUNT_CONV_TIME_140US           = const(0x0000)
_SHUNT_CONV_TIME_204US           = const(0x0008)
_SHUNT_CONV_TIME_332US           = const(0x0010)
_SHUNT_CONV_TIME_588US           = const(0x0018)
_SHUNT_CONV_TIME_1MS             = const(0x0020)     # 1.1ms, default
_SHUNT_CONV_TIME_2MS             = const(0x0028)     # 2.116ms
_SHUNT_CONV_TIME_4MS             = const(0x0030)     # 4.156ms
_SHUNT_CONV_TIME_8MS             = const(0x0038)     # 8.244ms

_MODE_MASK                       = const(0x0007)
_MODE_POWER_DOWN                 = const(0x0000)     # Power-down
_MODE_SHUNT_VOLTAGE_TRIGGERED    = const(0x0001)     # Shunt voltage, single-shot (triggered)
_MODE_BUS_VOLTAGE_TRIGGERED      = const(0x0002)     # Bus voltage, single-shot (triggered)
_MODE_SHUNT_AND_BUS_TRIGGERED    = const(0x0003)     # Shunt and bus, single-shot (triggered)
_MODE_POWER_DOWN2                = const(0x0004)     # Power-down
_MODE_SHUNT_VOLTAGE_CONTINUOUS   = const(0x0005)     # Shunt voltage, continous
_MODE_BUS_VOLTAGE_CONTINUOUS     = const(0x0006)     # Bus voltage, continuous
_MODE_SHUNT_AND_BUS_CONTINOUS    = const(0x0007)     # Shunt and bus, continuous (default)

# Other registers
_REG_SHUNT_VOLTAGE_CH            = (None, const(0x01), const(0x03), const(0x05))
_REG_BUS_VOLTAGE_CH              = (None, const(0x02), const(0x04), const(0x06))
_REG_CRITICAL_ALERT_LIMIT_CH     = (None, const(0x07), const(0x09), const(0x0B))
_REG_WARNING_ALERT_LIMIT_CH      = (None, const(0x08), const(0x0A), const(0x0C))
_REG_SHUNT_VOLTAGE_SUM           = const(0x0D)
_REG_SHUNT_VOLTAGE_SUM_LIMIT     = const(0x0E)

# Mask/enable register
_REG_MASK_ENABLE                 = const(0x0F)
_SUM_CONTROL_CH                  = (None,const(0x4000),const(0x2000),const(0x1000)) #default not set
_WARNING_LATCH_ENABLE            = const(0x0800)     # default not set
_CRITICAL_LATCH_ENABLE           = const(0x0400)     # default not set
_CRITICAL_FLAG_CH                = (None,const(0x0200),const(0x0100),const(0x0080))
_SUM_ALERT_FLAG                  = const(0x0040)
_WARNING_FLAG_CH                 = (None,const(0x0020),const(0x0010),const(0x0008))
_POWER_ALERT_FLAG                = const(0x0004)
_TIMING_ALERT_FLAG               = const(0x0002)
_CONV_READY_FLAG                 = const(0x0001)

# Other registers
_REG_POWER_VALID_UPPER_LIMIT     = const(0x10)
_REG_POWER_VALID_LOWER_LIMIT     = const(0x11)
_REG_MANUFACTURER_ID             = const(0xFE)
_REG_DIE_ID                      = const(0xFF)

# Constants for manufacturer and device ID
_MANUFACTURER_ID                 = const(0x5449)     # "TI"
_DIE_ID                          = const(0x3220)



INA3221_I2C_ADDR = const(64)
INA3221_REG_MASK = const(0x0f)
INA3221_REG_ID = const(0xff)
R_SHUNT = [100, 100, 100]

class INA3221:
    def __init__(self, i2c,addr = INA3221_I2C_ADDR):
        self.addr = addr
        self.i2c = i2c
        self.buf = bytearray(2)
    def getVShuntRaw(self, chl_num = 0):
        """获取分压电阻原始数据"""
        reg = 1 + chl_num * 2
        v_shunt_raw = self.i2c.readfrom_mem(self.addr, reg, 2)
        return v_shunt_raw

    def getVBusRaw(self, chl_num = 0):
        """获取输入电压原始数据"""
        reg = (chl_num + 1)* 2
        v_bus_raw = self.i2c.readfrom_mem(self.addr, reg, 2)
        return v_bus_raw
	
    def getVBus(self, chl_num = 0):
        """获取输入电压"""
        v_bus_raw = self.getVBusRaw(chl_num)
        v_bus = v_bus_raw[0]  * 256 + v_bus_raw[1]
        return v_bus

    
    def getIShunt(self, chl_num = 0):
        """获取chl_num电流"""
        v_shunt_raw = self.getVShuntRaw(chl_num)
        v_shunt = v_shunt_raw[1] * 5 + v_shunt_raw[0] * 1280
        i_shunt = v_shunt / R_SHUNT[chl_num]
        return i_shunt
    def getI(self,chl_num=0,avg=20):
        """获取电流，默认1ms一次，20ms为一次测量电流,0.02秒一次"""
        a=0
        for i in range(avg):
            while True:
                i_o=self.getIShunt(chl_num)
                if i_o<2000:
                    #inna最大电流为1.6A，超过2A的为错误值
                    break
            a=a+i_o   
#             time.sleep_ms(1)
        return round(a/avg,1)