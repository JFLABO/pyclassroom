# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 09:13:55 2020

@author: Administrator
"""

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# URLの指定
html = urlopen("https://www.oreilly.co.jp/ebook/")
bsObj = BeautifulSoup(html, "html.parser")

# テーブルを指定
table = bsObj.findAll("table", {"class":"tablesorter"})[0]
rows = table.findAll("tr")

with open("ebooks.csv", "w", encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)