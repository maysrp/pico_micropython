from time import sleep_us,ticks_ms
from machine import UART
class myUART(UART):
    def readUntil(self, termination, maxlen=-1, includeTermination=True):
        result = ''
        start = ticks_ms()
        while maxlen < 0 or len(result) < maxlen :
            if self.any():
                #print("here")
                result += chr(self.read(1)[0])
                #print(result)
                if result.endswith(termination):
                    if not includeTermination:
                        result = result[:-len(termination)]
                    break
            sleep_us(10)
        return result
    def readall(self):
        e=''
        while self.any():
            e=e+chr(self.read(1)[0])
        self.allr=e
        return e
