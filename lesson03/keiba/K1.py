# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
import signal
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from collections import deque
import datetime
import threading
import time
from PyQt5.QtWebEngineWidgets import QWebEngineView
#ボタンをクリックしたらIPATを開く
def IPAT_Button():
    initurl = 'https://www.ipat.jra.go.jp/'
    win.webEngineView.load(QUrl(initurl))
#ボタンをクリックしたらIPATを開く
def Home_Button():
    initurl = 'https://yoso.netkeiba.com/nar/?pid=race_list'
    win.webEngineView.load(QUrl(initurl))
 #ボタンをクリックしたらIPATを開く
def first_Button():
    initurl = 'http://first-onek.com/?c=contents_list'
    win.webEngineView.load(QUrl(initurl))
 #ボタンをクリックしたらIPATを開く
def grid_Button():
    initurl = 'https://docs.google.com/spreadsheets/d/1xJmg_lO39K-ry3eelJs8jQJ7GG4famXv5BRGM_FEzNo/edit#gid=0'
    win.webEngineView.load(QUrl(initurl))
def nittei_Button():
    initurl = 'http://www2.keiba.go.jp/KeibaWeb/TodayRaceInfo/TodayRaceInfoTop'
    win.webEngineView.load(QUrl(initurl)) 
def SIVA_Button():
    initurl = 'https://mail.siva-ai.com/dashboard'
    win.webEngineView.load(QUrl(initurl))
#from lib import functions
#from lib import gl
app = QtWidgets.QApplication([])
 
win = uic.loadUi("ui/keibamainWideScreen.ui") #specify the location of your .ui file
#win.resize(1024,1000)
win.show()

win.back_button.clicked.connect(win.webEngineView.back)   
win.IPAT_Button.clicked.connect(IPAT_Button)
win.HomeButton.clicked.connect(Home_Button)
win.grid_Button.clicked.connect(grid_Button) 
win.first_Button.clicked.connect(first_Button)
win.nittei_Button.clicked.connect(nittei_Button) 
win.SIVA_Button.clicked.connect(SIVA_Button) 
initurl = 'https://yoso.netkeiba.com/nar/?pid=race_list&kaisai_date=20200128'
win.webEngineView.load(QUrl(initurl))   
#win.IPAT_Button = QPushButton('IPAT_Button', self)
#win.IPAT_Button.clicked.connect(IPAT_Button(self)) 


sys.exit(app.exec())
