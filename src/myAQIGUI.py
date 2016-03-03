#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import matplotlib  

from matplotlib import dates
from datetime import datetime,timedelta

# matplotlib采用WXAgg为后台,将matplotlib嵌入wxPython中  
matplotlib.use("WXAgg")  
  
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas  
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar  
from matplotlib.ticker import MultipleLocator, FuncFormatter  
  
import pylab  
from matplotlib import pyplot 

import dataCollect
from Queue import Queue, Empty
from threading import Thread

EVENT_TIMER = 'eTimer'


###########################################################################
## Event type
###########################################################################
class Event(object):

    #----------------------------------------------------------------------
    def __init__(self, handle, type_=None):
        """Constructor"""
        self.handle = handle
        self.type_ = type_     



class MainFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"MyAQI", \
            pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        #####################################################
        # Manual Add Code

        self.dpi = 100
        # self.Figure = matplotlib.figure.Figure(figsize=(10,3), dpi=self.dpi)
        self.Figure = matplotlib.figure.Figure(figsize=(50,30))
        # self.axes = self.Figure.add_axes([0.1,0.1,0.8,0.8])
        self.axes25 = self.Figure.add_subplot(111)
        self.axes10 = self.axes25.twinx()

        self.FigureCanvas = FigureCanvas(self,-1,self.Figure) 
        #####################################################

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        MainSizer = wx.FlexGridSizer( 1, 3, 0, 0 )
        MainSizer.SetFlexibleDirection( wx.BOTH )
        MainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
        

        leftSizer = wx.FlexGridSizer( 7, 1, 0, 0 )
        leftSizer.SetFlexibleDirection( wx.BOTH )
        leftSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )


        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        leftSizer.Add( self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5 )
        
        self.m_btn_start = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        leftSizer.Add( self.m_btn_start, 0, wx.ALL | wx.EXPAND, 5 )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        leftSizer.Add( self.m_staticText2, 0, wx.ALL | wx.EXPAND, 5 )
        
        self.m_btn_stop = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        leftSizer.Add( self.m_btn_stop, 0, wx.ALL | wx.EXPAND, 5 )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        leftSizer.Add( self.m_staticText3, 0, wx.ALL | wx.EXPAND, 5 )
        
        self.m_btn_quit = wx.Button( self, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
        leftSizer.Add( self.m_btn_quit, 0, wx.ALL | wx.EXPAND, 5 )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        leftSizer.Add( self.m_staticText4, 0, wx.ALL | wx.EXPAND, 5 )
        

        MainSizer.Add( leftSizer, 1, wx.ALL | wx.EXPAND, 5 )
        
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        MainSizer.Add( self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5 )

        MainSizer.Add(self.FigureCanvas,proportion =-10, border = 2,flag = wx.ALL | wx.GROW)  
        
        
        self.SetSizer( MainSizer )
        self.Layout()

        self.timer = wx.Timer()
        self.timer.SetOwner( self, wx.ID_ANY )
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btn_start.Bind( wx.EVT_BUTTON, self.onStart )
        self.m_btn_stop.Bind( wx.EVT_BUTTON, self.onStop )
        self.m_btn_quit.Bind( wx.EVT_BUTTON, self.onQuit )
        self.Bind( wx.EVT_TIMER, self.onTimer, id=wx.ID_ANY )




        # Create object for AQI data

        self.tickerData = dataCollect.AQIdata()

        # initial plot the graphy here, only need to update data later

        # self.plot(self.tickerData.xTicker,self.tickerData.y25Ticker, '--+r', self.tickerData.xTicker,self.tickerData.y10Ticker,'--*g')  
        self.plot_data25 = self.axes25.plot(self.tickerData.xTicker,self.tickerData.y25Ticker,'-+r')[0]  
        self.plot_data10 = self.axes10.plot(self.tickerData.xTicker,self.tickerData.y10Ticker,'-*g')[0]  

        self.axes25.set_axis_bgcolor('gray')

        self.axes25.set_ybound(lower=0, upper=500)
        self.axes10.set_ybound(lower=0, upper=500)

        # hfmt = dates.DateFormatter('%m/%d %H:%M')
        hfmt = dates.DateFormatter('%H:%M')
        # self.axes25.xaxis.set_major_locator(dates.MinuteLocator())
        self.axes25.xaxis.set_major_locator(dates.HourLocator())
        self.axes25.xaxis.set_major_formatter(hfmt)
        # self.axes10.xaxis.set_major_locator(dates.MinuteLocator())
        self.axes25.xaxis.set_major_locator(dates.HourLocator())
        self.axes10.xaxis.set_major_formatter(hfmt)    

        
        # self.axes25.get_xticklabels(), fontsize=8)
        # self.axes25.get_yticklabels(), fontsize=8)
        # self.axes10.get_xticklabels(), fontsize=8)
        # self.axes10.get_yticklabels(), fontsize=8)

        
        self.sleepTime = 10000


        self.__queue = Queue()
        self.__active = False

    
    def __del__( self ):
        self.timer.Stop()
        if self.__active == True:
            self.__active = False
            self.__thread.join()   
    
    # Virtual event handlers, overide them in your derived class
    def onStart( self, event ):
        self.timer.Start(self.sleepTime)
        if self.__active == False:
            self.__thread = Thread(target = self.__run)
            self.__active  = True
            self.__thread.start()    

    def onStop( self, event ):
        self.timer.Stop()
        if self.__active == True:
            self.__active = False
            self.__thread.join() 
        
    
    def onQuit( self, event ):
        self.timer.Stop()
        if self.__active == True:
            self.__active = False
            self.__thread.join() 
        self.Close()

    def onTimer( self, event ):

        event_ = Event(self.updateGraphy, type_=EVENT_TIMER)
        self.__queue.put(event_)

    def updateGraphy(self):
        self.tickerData.updateElement(self.sleepTime)
        self.__plot()


    def __run(self):
        while self.__active == True:
            try:
                event_ = self.__queue.get(block = True, timeout = 1)  
                self.__process(event_)
            except Empty:
                pass       


    def __process(self, event_):
        event_.handle()

    def __plot(self,*args,**kwargs):  
        '''update the plot here'''

         # how to change the x axis to time format

        dts = map(datetime.fromtimestamp, self.tickerData.xTicker)
        fds = dates.date2num(dts) # converted

        xmin = fds[0]
        xmax = fds[-1]+0.001

        diff = dts[-1]-dts[0]


        ymin = 0
        ymax = max(max(self.tickerData.y25Ticker), max(self.tickerData.y10Ticker))*1.5

        self.axes25.set_xbound(lower=xmin, upper=xmax)
        self.axes25.set_ybound(lower=ymin, upper=ymax)

        self.axes10.set_xbound(lower=xmin, upper=xmax)
        self.axes10.set_ybound(lower=ymin, upper=ymax)

        # X axis format setting
        if diff < timedelta(minutes=20):
            hfmt = dates.DateFormatter('%H:%M')
            self.axes25.xaxis.set_major_formatter(hfmt)
            self.axes25.xaxis.set_major_locator(dates.MinuteLocator(byminute=range(60), interval=2))
            self.axes25.xaxis.set_minor_locator(dates.MinuteLocator(interval=1))

        elif diff < timedelta(hours=1):
            hfmt = dates.DateFormatter('%H:%M')
            self.axes25.xaxis.set_major_formatter(hfmt)
            self.axes25.xaxis.set_major_locator(dates.MinuteLocator(byminute=range(60), interval=5))
            self.axes25.xaxis.set_minor_locator(dates.MinuteLocator(interval=2))

        elif diff < timedelta(hours=6):
            hfmt = dates.DateFormatter('%H:%M')
            self.axes25.xaxis.set_major_formatter(hfmt)
            self.axes25.xaxis.set_major_locator(dates.HourLocator(interval=1))
            self.axes25.xaxis.set_minor_locator(dates.MinuteLocator(interval=15))

        elif diff < timedelta(days=2):
            hfmt = dates.DateFormatter('%H:%M')
            self.axes25.xaxis.set_major_formatter(hfmt)
            self.axes25.xaxis.set_major_locator(dates.HourLocator(interval=4))
            self.axes25.xaxis.set_minor_locator(dates.HourLocator(interval=1))


        elif diff < timedelta(days=10):
            hfmt = dates.DateFormatter('%m/%d')
            self.axes25.xaxis.set_major_formatter(hfmt)
            self.axes25.xaxis.set_major_locator(dates.DayLocator(interval=1))
            self.axes25.xaxis.set_minor_locator(dates.HourLocator(interval=6))

        elif diff < timedelta(days=40):
            hfmt = dates.DateFormatter('%m/%d')
            self.axes25.xaxis.set_major_formatter(hfmt)
            self.axes25.xaxis.set_major_locator(dates.DayLocator(interval=2))




        self.plot_data25.set_xdata(fds)
        self.plot_data25.set_ydata(self.tickerData.y25Ticker)

        self.plot_data10.set_xdata(fds)
        self.plot_data10.set_ydata(self.tickerData.y10Ticker)

        xlabels = self.axes25.get_xticklabels()
        for xl in xlabels:
            xl.set_rotation(45) 


        self.__updatePlot()  

    def __updatePlot(self):  
        '''''need to use this function update graphy if any data updated '''  
        self.FigureCanvas.draw()    

    


     



if __name__ == '__main__':

    app = wx.App()
    # wx.InitAllImageHandlers()
    frame = MainFrame(None)
    app.SetTopWindow(frame)
    
    frame.Show()
    
    app.MainLoop()
    
    

