#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' 
This file is reserved for Data collection
Output: Time, x, y for PM2.5 and PM10

'''

import time
import random
from datetime import datetime
import numpy as np
import serial
import binascii


class AQIdata(object):
    def __init__(self):
        self.timeStamp = 0
        self.timeStr = ''
        self.pm25 = 0
        self.pm10 = 0

        # self.xtimeList = []
        # self.y25List = []
        # self.y10List = []

        self.xTicker = np.array([])
        self.y25Ticker = np.array([])
        self.y10Ticker = np.array([])

        self.rs232 = serial.Serial('com3',9600)

    def __del__( self ):
        self.rs232.close() 



    def __getAQIdata(self):

        


        avrgnum = 1.0


        # # random data for debug purpose
        # self.pm25 = random.random()
        # self.pm10 = random.random()

        # clear RS232 Buffer
        self.rs232.flushInput()
        self.rs232.flushOutput()

        # totall 32 byte for each frame starting with 42 4d
        # make sure data start from 42&4d, if not, clear the rest
        str = ''
        while True:
            temp = str
            str = self.rs232.read(1)
            str = binascii.b2a_hex(str)
             
            if temp=='42' and str =='4d':
                str = self.rs232.read(30)    # clear the following 30 bytes
                break


        pm25qty = 0
        pm10qty = 0

        self.timeStamp = time.time()
        self.timeStr = time.strftime('%d%b%Y_%H%M%S', time.localtime(self.timeStamp))

        for i in range(int(avrgnum)):
             
            str = self.rs232.read(32) 
            pm25qty = int(binascii.b2a_hex(str[6]),16)*256+int(binascii.b2a_hex(str[7]),16) + pm25qty
            pm10qty = int(binascii.b2a_hex(str[8]),16)*256+int(binascii.b2a_hex(str[9]),16) + pm10qty

        pm25qty = pm25qty/avrgnum
        pm10qty = pm10qty/avrgnum

        self.pm25 = self.__qty2aqi(pm25qty)
        self.pm10 = self.__qty2aqi(pm10qty)

        print self.pm25
        print self.pm10


             



    def updateElement(self, sleepTime):

        self.sleepTime = sleepTime
        
        self.__getAQIdata()

        self.xTicker = np.append(self.xTicker, self.timeStamp)
        self.y25Ticker = np.append(self.y25Ticker, self.pm25)
        self.y10Ticker = np.append(self.y10Ticker, self.pm10)

        # self.xtimeList.append(self.timeStamp)
        # self.y25List.append(self.pm25)
        # self.y10List.append(self.pm10)

    def __qty2aqi(self, qty):
        '''
        using standard from USA
        '''
        if qty <= 15.4:
            Clow = 0
            Chigh = 15.4
            Ilow = 0
            Ihigh = 50

        elif qty <= 40.4:
            Clow = 15.5
            Chigh = 40.4
            Ilow = 51
            Ihigh = 100

        elif qty <= 65.4:
            Clow = 40.5
            Chigh = 65.4
            Ilow = 101
            Ihigh = 150

        elif qty <= 150.4:
            Clow = 65.5
            Chigh = 150.4
            Ilow = 151
            Ihigh = 200

        elif qty <= 250.4:
            Clow = 150.5
            Chigh = 250.4
            Ilow = 201
            Ihigh = 300

        elif qty <= 350.4:
            Clow = 250.5
            Chigh = 350.4
            Ilow = 301
            Ihigh = 400

        elif qty <= 500.4:
            Clow = 350.5
            Chigh = 500.4
            Ilow = 401
            Ihigh = 500
        else:
            return 1000
        aqi = (((Ihigh-Ilow)/(Chigh-Clow))*(qty-Clow))+Ilow
        return aqi





class AQIdata2(object):
    ''' 
    for debug purpose.
    created data randomly
    '''
    def __init__(self):
        self.timeStamp = 0
        self.timeStr = ''
        self.pm25 = 0
        self.pm10 = 0

        # self.xtimeList = []
        # self.y25List = []
        # self.y10List = []

        self.xTicker = np.array([])
        self.y25Ticker = np.array([])
        self.y10Ticker = np.array([])


    def __del__( self ):
        pass



    def __getAQIdata(self):

        # random data for debug purpose
        self.pm25 = random.random()*10+150
        self.pm10 = random.random()*10+130

        self.timeStamp = time.time()
        self.timeStr = time.strftime('%d%b%Y_%H%M%S', time.localtime(self.timeStamp))


    def updateElement(self, sleepTime):

        self.sleepTime = sleepTime
        
        self.__getAQIdata()

        self.xTicker = np.append(self.xTicker, self.timeStamp)
        self.y25Ticker = np.append(self.y25Ticker, self.pm25)
        self.y10Ticker = np.append(self.y10Ticker, self.pm10)


def runTimer():
    time.sleep(1)


if __name__ == '__main__':

    a = AQIdata()

    for i in range(0,100):

        a.updateElement()
        print a.y25Ticker

        runTimer()



