#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' 
This file is reserved for Data collection
Output: Time, x, y for PM2.5 and PM10

'''

import time
import random
from datetime import datetime


class AQIdata(object):
    def __init__(self):
        self.timestamp = 0
        self.pm25 = 0
        self.pm10 = 0

def getAQIdata(data):

    data.timestamp = datetime.now().strftime('%d%b%Y_%H%M%S')
    data.pm25 = random.random()
    data.pm10 = random.random()
    return data

def runTimer():
    time.sleep(1)


if __name__ == '__main__':
    for i in range(0,100):
        a = AQIdata()
        getAQIdata(a)
        print a.pm25
        print a.pm10
        print a.timestamp
        runTimer()



