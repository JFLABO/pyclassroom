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
def View_Button():
    textBox = win.url.text()
    initurl = textBox
    win.webEngineView.load(QUrl(initurl))
    #win.viewurl.setText("aaa")
def handle_url_change():
    #win.viewurl = win.url.text()
    #win.viewurl="aaa"
    s=win.webEngineView.url()
    s=str(s)
    win.viewurl.setText(s)
#ボタンをクリックしたらIPATを開く
def Home_Button():
    initurl = 'https://yoso.netkeiba.com/nar/?pid=race_list'
    win.webEngineView.load(QUrl(initurl))
#ボタンをクリックしたらIPATを開く
def url_make():
    initurl = 'http://www2.keiba.go.jp/KeibaWeb/TodayRaceInfo/OddsTanFuku?k_raceDate='+'2020%2f01%2f29&k_raceNo=7&k_babaCode=28'
    win.webEngineView.load(QUrl(initurl))

app = QtWidgets.QApplication([])
 
win = uic.loadUi("ui/keibaozz.ui") #specify the location of your .ui file
#win.resize(1024,1000)
win.comboBox_year.addItems(['2020', '2019', '2018'])
win.comboBox_month.addItems(['01', '02', '03'])
win.comboBox_race_code.addItems(['31', '21', '24', '28'])
win.Home_Button.clicked.connect(Home_Button)
win.comboBox_day.addItems(['01', '02', '03'])
win.comboBox_RNO.addItems(['01', '02', '03'])
win.show()
win.back_button.clicked.connect(win.webEngineView.back)   
win.View_Button.clicked.connect(View_Button)
win.webEngineView.urlChanged.connect(handle_url_change)
initurl = 'https://yoso.netkeiba.com/nar/?pid=race_list&kaisai_date=20200128'
win.webEngineView.load(QUrl(initurl))   


sys.exit(app.exec())
