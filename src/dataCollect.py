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

        # self.xtimeList = []
        # self.y25List = []
        # self.y10List = []

        self.xTicker = np.array([])
        self.y25Ticker = np.array([])
        self.y10Ticker = np.array([])



    def __getAQIdata(self):

        self.timeStamp = time.time()
        self.timeStr = time.strftime('%d%b%Y_%H%M%S', time.localtime(self.timeStamp))
        self.pm25 = random.random()
        self.pm10 = random.random()


    def updateElement(self):
        self.__getAQIdata()

        self.xTicker = np.append(self.xTicker, self.timeStamp)
        self.y25Ticker = np.append(self.y25Ticker, self.pm25)
        self.y10Ticker = np.append(self.y10Ticker, self.pm10)

        # self.xtimeList.append(self.timeStamp)
        # self.y25List.append(self.pm25)
        # self.y10List.append(self.pm10)


def runTimer():
    time.sleep(1)


if __name__ == '__main__':

    a = AQIdata()

    for i in range(0,100):

        a.updateElement()
        print a.y25Ticker

        runTimer()



