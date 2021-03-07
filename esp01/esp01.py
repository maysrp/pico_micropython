from machine import UART
import utime

"""
The MicroPython port for Pi Pico has no timeout for readline() at this moment.
We use this hack to make sure it won't get stuck forever.
"""

class uartTimeOut(UART):

   def readline(self, timeOut=100):
       if timeOut is None:
           return super().readline()
       else:
           now = utime.ticks_ms()
           data = b''
           while True:
               if utime.ticks_ms()-now > timeOut:
                   break
               else:
                   if super().any():
                       _d = super().read(1)
                       data += _d
                       if "\n" in _d:
                           break
           return data

class wifi(object):
    def __init__(self,uart=1,baud_rate=9600):
        self.uart=uartTimeOut(uart, baud_rate)
    def _set_command(self,command):
        re=self.uart.write(command)
        if self.uart.any():
            return re.readline()
    def set_cwmode(self,inx=1):
        cod="AT+CWMODE="+str(inx)+"\r"
        return self._set_command(cod)
    def wifi(self,name,password):
        cod='AT+CWJAP="%s","%s"' % (name,password)
        return self._set_command(cod)
    def cipmux(self,num=0):
        cod='AT+CIPMUX="%s"' % (num,)
        return self._set_command(cod)
    def http(self,url,)
    
