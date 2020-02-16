# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:21:18 2020

@author: Administrator
時間管理：あとどのくらいの時間があるか？
価格管理：リアルタイム取得
勝つための哲学：メンタル強化　勝ち組　FX
経済システムに強い　安定して資産を増やすシステムだった。
メンタルサポートシステム

F1.スレッドで値動きを取得
F2.目標レートを上回っています
F3.「○○」するといいと思います。
　売り買い

F4.タイマー
AI:現在時刻はXX:XXです。
目標時間まであと何分です。1時間　30分　15分　5分
龍と贔屓とヤアズにお願い。金運をため込んで

目標レートをxxpips達成しています。資産が増えました。

F5.しゃべる
時刻をお知らせ
import  subproces

subprocess.run("echo \""+key+"\" | open_jtalk -x /var/lib/mecab/dic/open-jtalk/naist-jdic -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -ow /dev/stdout | aplay "
  ,shell=True
  ,stdout=subprocess.DEVNULL
  ,stderr=subprocess.DEVNULL)
  
間隔を設定
通貨ペアと目標レートを設定　差を表示
AI：応答　応援お願いします。

みんなありがとう。もっと上がるといいなぁ　すざくとりゅうにおねがい　かたせて
python -m pip install pywin32
現在時刻を読み上げる

新鮮なレートの取得

原稿を読む

時刻の設定　現在時刻の取得

変数を連結してスレッド読む

退屈　Pyhon

タイマー設定音声コール asterisk　内線通知

テキストボックスにJSONを入れる

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
app = QtWidgets.QApplication([])
app.setWindowIcon(QIcon('jflabo.png'))
print("\007")
                  
def say_mess():
    speech = win32com.client.Dispatch("Sapi.SpVoice")
    #speech.Speak("Hello Pythonスリー World!きんうんひきよせ　いま03:45です")
    #speech.Speak("やった　みんなありがとう。目標レートまでもう少し")
    #speech.Speak("日本時間の05:10分くらいからあと10分でユーロドルもっとさがるといいな")
    #speech.Speak("あぽろん　アレックス　次の判定は日本時間の05:にじゅう分")
    #speech.Speak("このプロジェクトチームにお願いしたい方針はつねにじょうきげんで、ゆうがにかまえていること")
    #speech.Speak("みんなで協力すればきっとうまくいくよ　つぎのはんていまであと約1時間ちょうどです。今日も明るく元気に余裕で勝ちましょう")
    #speech.Speak("地球　世界に平和と繁栄　祝福を　we trust god bless you.thank you そーまっち.グラッツェ　メルシー")
    #speech.Speak("わたしたちはコロナウイルス　感染症にかかっている人たちの救済イト治療をやるよ　助けてあげたいんだ")   
win = uic.loadUi("ui/FXTrade.ui") #specify the location of your .ui file
win.resize(1024,700)
win.show()
#with open('data/test.json') as f:
#    df = json.load(f)

#文字列加工　データ処理
f = open(r'data/test.json','r',encoding="utf-8_sig")
data = json.load(f)
#print(data)

pprint.pprint(data, width=40)
win.textEdit.setText(str(data))
win.pushButton.clicked.connect(say_mess)
#say_mess()


sys.exit(app.exec())
