# -*- coding: utf-8 -*-
import sys
import requests
import lxml.html
import re
import csv
from PyQt5 import QtWidgets, uic
import signal
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from collections import deque
import datetime
import threading
import time
from PyQt5.QtWebEngineWidgets import QWebEngineView
class MyTableModel(QAbstractTableModel):
    def __init__(self, list, headers = [], parent = None):
        QAbstractTableModel.__init__(self, parent)
        self.list = list
        self.headers = headers

    def rowCount(self, parent):
        return len(self.list)

    def columnCount(self, parent):
        return len(self.list[0])

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def data(self, index, role):
        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            return self.list[row][column]

        if role == Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.list[row][column]
            return value

    def setData(self, index, value, role = Qt.EditRole):
        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            self.list[row][column] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def headerData(self, section, orientation, role):

        if role == Qt.DisplayRole:

            if orientation == Qt.Horizontal:

                if section < len(self.headers):
                    return self.headers[section]
                else:
                    return "not implemented"
            else:
                return "item %d" % section
def main():
    url = "https://nar.netkeiba.com/?pid=race&id=c202048013101&mode=top" #コマンドライン引数からURLを取得
    html = fetch(url) #URLのWebページを取得
    result = scrape(html) #取得したWebページから欲しい部分のみを切り出す
#    save('result.csv',result) #切り出した結果をCSVに保存する

def fetch(url :str): 
    r = requests.get(url) #urlのWebページを保存する
    r.encoding = r.apparent_encoding #文字化けを防ぐためにencodingの値をappearent_encodingで判定した値に変更する
    return r.text #取得データを文字列で返す
"""
## テーブルの初期化
tableWidget.clear()
items = [('hoge', 'HOGE'), ('fuga', 'FUGA'), ('piyo', 'PIYO')]
## 行数の設定
tableWidget.setRowCount(len(items))
## 要素の追加
r = 0
for item in items:

    tableWidget.setItem(r, 0, QtGui.QTableWidgetItem(item[0]))

    tableWidget.setItem(r, 1, QtGui.QTableWidgetItem(item[1]))

    r += 1
"""
def scrape(html: str):
    html = lxml.html.fromstring(html) #fetch()での取得結果をパース
    result = [] #スクレイピング結果を格納
    
    for h in html.cssselect('#race_main > div > table > tr'):#スクレイピング箇所をCSSセレクタで指定
        column = ((",".join(h.text_content().split("\n"))).lstrip(",").rstrip(",")).split(",")
        #text_content()はcssselectでマッチした部分のテキストを改行文字で連結して返すので、
        #splitを使って改行文字で分割して、その結果をカンマ区切りでjoinする。
        #前と後ろに余計な空白とカンマが入っている(tdじゃなくてtrまでのセレクタをしていした分の空文字が入っちゃってる?ようわからん)ので、
        #splitで空白を、lstrip,rstripでカンマを削除してさらにそれをカンマで区切ってリストにしている
        print(column)
        column.pop(4) if column[4] == "" else None  #1行目以外、馬名と性齢の間に空文字が入っちゃってるので取り出す
        result.append(column) #リストに行のデータ(リストを追加)
        
    win.result_view.setPlainText(str(result))
    headers = ["000", "001", "002"]
    tableData0 = result
    
    model = MyTableModel(tableData0, headers)
    win.tableView.setModel(model)
    return result #結果を返す
def scrape2(html: str):
    html = lxml.html.fromstring(html) #fetch()での取得結果をパース
    result = [] #スクレイピング結果を格納
    for h in html.cssselect('.race_table_01 > tr'):#スクレイピング箇所をCSSセレクタで指定
        column = ((",".join(h.text_content().split("\n"))).lstrip(",").rstrip(",")).split(",")
        #text_content()はcssselectでマッチした部分のテキストを改行文字で連結して返すので、
        #splitを使って改行文字で分割して、その結果をカンマ区切りでjoinする。
        #前と後ろに余計な空白とカンマが入っている(tdじゃなくてtrまでのセレクタをしていした分の空文字が入っちゃってる?ようわからん)ので、
        #splitで空白を、lstrip,rstripでカンマを削除してさらにそれをカンマで区切ってリストにしている
        column.pop(4) if column[4] == "" else None  #1行目以外、馬名と性齢の間に空文字が入っちゃってるので取り出す
        result.append(column) #リストに行のデータ(リストを追加)
        print(column)
    win.result_view.setPlainText(str(result))
    win.tableView.clearSpans ()
    headers = ["000", "001", "002"]
    tableData0 = result
    
    model = MyTableModel(tableData0, headers)
    win.tableView.setModel(model)
    return result #結果を返す
def save(file_path, result):
     with open(file_path, 'w', newline='') as f: #ファイルに書き込む
         writer = csv.writer(f) #ファイルオブジェクトを引数に指定する
         try:
             importer = result.pop(0)
         except IndexError as e:
             print(e)
         writer.writerow(result.pop(0)) #一行目のフィールド名を書き込む
         writer.writerows(result) #残りの行を書き込む
def main2(s):
    url = s #コマンドライン引数からURLを取得
    html = fetch(url) #URLのWebページを取得
    result = scrape2(html) #取得したWebページから欲しい部分のみを切り出す
#    save('result.csv',result) #切り出した結果をCSVに保存する
    
def View_Button():
    #textBox = win.url.text()
    initurl = win.lineEdit.text()
    main2(initurl)
    #win.webEngineView.load(QUrl(initurl))
    #win.viewurl.setText("aaa")
app = QtWidgets.QApplication([])
 
win = uic.loadUi("ui/serchwin.ui") #specify the location of your .ui file
win.comboBox_year.addItems(['2020', '2019', '2018'])
win.comboBox_month.addItems(['01', '02', '03'])
win.comboBox_race_code.addItems(['31', '21', '24', '28'])
win.View_Button.clicked.connect(View_Button)
win.comboBox_day.addItems(['01', '02', '03'])
win.comboBox_RNO.addItems(['01', '02', '03'])
win.show()
#win.View_Button.clicked.connect(View_Button)
main()
    

            
sys.exit(app.exec())
