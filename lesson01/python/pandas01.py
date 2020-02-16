# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 09:25:59 2020

@author: Administrator
"""

import pandas as pd

data=""

def printcsv(i):
    global data
    #df = pd.read_csv('data/HHaitouKabu01-P'+str(i)+'.csv', header=None, skiprows=2)
    df = pd.read_csv('data/HHaitouKabu01-P'+str(i)+'.csv')
    print(df)
    #data=data+df
    with open("data/KABULIST.csv", "a", encoding='utf-8') as file:
        #print(data, file=file)
        #global data
        writer = csv.writer(file)
        writer.writerow(df)
    #print(df.index)
#    11  12  13  14
# 0  21  22  23  24
# 1  31  32  33  34

#print(df.columns)
for i in range(1, 5):
    printcsv(i)



#並べ替え　安くて高配当　つぶれない株　割安株
#どういう株を買えばいいか