# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:21:18 2020

@author: Administrator


"""
import sys
import win32com.client
from PyQt5 import QtWidgets, uic
import signal
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
import json
from collections import OrderedDict
import pprint
from PyQt5.QtWebEngineWidgets import QWebEngineView
def View_Button():
    #win.label1.setText(Qlabel(str))
    win.label1.setText("str")
    win.lineEdit.setText("aaaa")
    win.webEngineView.load(QUrl(initurl))
def act_combobox():
    win.label1.setText(win.comboBox.currentText())
    win.lineEdit.setText("aaaa")
    
app = QtWidgets.QApplication([])
#app.setWindowIcon(QIcon('jflabo.png'))
initurl = "https://fx-rashinban.com/b00001-JPY/a7801-%83h%83%8B%89~%8C%A9%92%CA%82%B5+109%89~%91%E4%8F%98%94%D5%82%D6%81A%8A%B4%90%F5%8Ag%91%E5%83%8A%83X%83N%82%C5%89%BA%97%8E%81i20%2F1%2F24%81j" #コマンドライン引数からURLを取得

win = uic.loadUi("ui/fxinfo.ui") #specify the location of your .ui file
#win.resize(1024,700)
win.comboBox.addItems(['01', '02', '03'])
#win.comboBox.activated[str].connect(act_combobox("str"))
#win.comboBox.connect(act_combobox("str"))
'''
 print 'ComboBox Index    = ', self.combo.currentIndex()
        print 'ComboBox Label    = ', self.combo.currentText()'''
win.comboBox.currentTextChanged.connect(act_combobox)
win.pushButton.clicked.connect(View_Button)
win.show()



    
'''
win.comboBox.Items.AddRange(System.Array[System.Object](
   ["Car",
   "Truck",
   "OpenCar",
   "Taxi",
   "SportsCar",
   "MiniCar"]))

win.comboBox.SelectedIndexChanged += self.ComboBoxSelectedIndexChanged

def ComboBoxSelectedIndexChanged(self, sender, e):
    win.label.Text = " is selected."

    self.ui.comboBox.activated[str].connect(self.act_combobox)
        self.ui.lineEdit.textEdited.connect(self.in_lineedit)

        self.show()

    def act_combobox(self, text):
        global json_dict
        self.ui.label_text.setText(text)
        for key in json_dict:
            if text == json_dict[key]["string"]:
                self.ui.lineEdit.setText(json_dict[key]["code"])
                   '''
sys.exit(app.exec())
