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


class AQIdata(object):
    def __init__(self):
        self.timeStamp = 0
        self.timeStr = ''
        self.pm25 = 0
        self.pm10 = 0

    def getAQIdata(self):

        self.timeStamp = time.time()
        self.timeStr = time.strftime('%d%b%Y_%H%M%S', time.localtime(self.timeStamp))
        self.pm25 = random.random()
        self.pm10 = random.random()

class DataHandle(object):
    def __init__(self, data):
        self.myAQIdata = data
        self.xTicker = np.array([])
        self.y25Ticker = np.array([])
        self.y10Ticker = np.array([])


    def updateElement(self):
        self.myAQIdata.getAQIdata()
        self.xTicker = np.append(self.xTicker, self.myAQIdata.timeStamp)
        self.y25Ticker = np.append(self.y25Ticker, self.myAQIdata.pm25)
        self.y10Ticker = np.append(self.y10Ticker, self.myAQIdata.pm10)




def runTimer():
    time.sleep(1)


if __name__ == '__main__':

    a = AQIdata()
    myDate = DataHandle(a)

    for i in range(0,100):

        myDate.updateElement()
        print myDate.y25Ticker

        runTimer()



