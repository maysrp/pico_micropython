
import time
class GPS(object):
    def __init__(self,gpsModule):
        self.buff = bytearray(255)
        self.TIMEOUT = False
        self.FIX_STATUS = False
        self.latitude = ""
        self.longitude = ""
        self.satellites = ""
        self.GPStime = ""
        self.gpsModule=gpsModule
    def getGPS(self):
        # global FIX_STATUS, TIMEOUT, latitude, longitude, satellites, GPStime
        gpsModule=self.gpsModule
        timeout = time.time() + 8
        while True:
            gpsModule.readline()
            buff = str(gpsModule.readline())
            parts = buff.split(',')

            if (parts[0] == "b'$GPGGA" and len(parts) == 15):
                if(parts[1] and parts[2] and parts[3] and parts[4] and parts[5] and parts[6] and parts[7]):
                    # print(buff)

                    self.latitude = self.convertToDegree(parts[2])
                    if (parts[3] == 'S'):
                        self.latitude = -self.latitude
                    self.longitude = self.convertToDegree(parts[4])
                    if (parts[5] == 'W'):
                        self.longitude = -self.longitude
                    self.satellites = parts[7]
                    self.GPStime = parts[1][0:2] + ":" + parts[1][2:4] + ":" + parts[1][4:6]
                    self.FIX_STATUS = True
                    break

            if (time.time() > timeout):
                self.TIMEOUT = True
                break
            time.sleep_ms(500)

    def convertToDegree(self,RawDegrees):

        RawAsFloat = float(RawDegrees)
        firstdigits = int(RawAsFloat/100)
        nexttwodigits = RawAsFloat - float(firstdigits*100)

        Converted = float(firstdigits + nexttwodigits/60.0)
        Converted = '{0:.6f}'.format(Converted)
        return str(Converted)

