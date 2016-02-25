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
  
# matplotlib采用WXAgg为后台,将matplotlib嵌入wxPython中  
matplotlib.use("WXAgg")  
  
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas  
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar  
from matplotlib.ticker import MultipleLocator, FuncFormatter  
  
import pylab  
from matplotlib import pyplot 


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"MyAQI", \
            pos = wx.DefaultPosition, size = wx.Size( 800,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        #####################################################
        # Manual Add Code
        self.Figure = matplotlib.figure.Figure(figsize=(100,20))
        self.axes = self.Figure.add_axes([0.1,0.1,0.8,0.8])  
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
        
        # bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        # leftSizer.Add( bSizer3, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        MainSizer.Add( leftSizer, 1, wx.ALL | wx.EXPAND, 5 )
        
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        MainSizer.Add( self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5 )

        MainSizer.Add(self.FigureCanvas,proportion =-10, border = 2,flag = wx.ALL | wx.EXPAND)  
        
        
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
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def onStart( self, event ):
        self.timer.Start(1000)
    
    def onStop( self, event ):
        self.timer.Stop()
    
    def onQuit( self, event ):
        self.Close()

    def onTimer( self, event ):
        print('Hello World')
        

if __name__ == '__main__':

    app = wx.App()
    # wx.InitAllImageHandlers()
    frame = MainFrame(None)
    app.SetTopWindow(frame)
    
    frame.Show()
    
    app.MainLoop()
    
    

